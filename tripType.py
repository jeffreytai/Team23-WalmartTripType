import csv
from math import log

# Dictionaries hold all unique values and respective support for trip type
visitNumberDict = {}
weekdayDict = {}
upcDict = {}
scanCountDict = {}
departmentDescriptionDict = {}
finelineNumberDict = {}

# Parameter: array of number(s)
# Output: information or average entropy
# Example: information([1,2,3]) = 0.918
# Example: information([1]) = 1.0
def information( support ):
    numValues = len(support)
    sumValues = sum(support)
    if numValues == 1:
        return 0.0
    else:
        info = 0.0
        for val in support:
            info += ( -(float(val)/sumValues) * log((float(val)/sumValues),2) )
    return info

# Calculates entropy for entire attribute
def calculateEntropy( dict ):
    copyDict = {}
    for key,value in dict.items():
        for k,v in value.items():
            if k in copyDict:
                copyDict[k] += v
            else:
                copyDict[k] = v

    return information(copyDict.values())

# Creates a dictionary of dictionaries
# Dictionary is a key-value pair of each unique visit number to a subdictionary
# Subdictionary contains key-value pairs of the TripType to its support
# Parameters: dict (specific dictionary), index (respective position in row), row (contains information for that entry)
def generateAttributeTable( dict, index, row ):
    # Handles case of Upc being empty
    if index == 3 and row[index] == '':
        return
    else:
        if row[index] in dict:
            if row[0] in dict[row[index]]:
                dict[row[index]][row[0]] += 1
            else:
                dict[row[index]][row[0]] = 1
        else:
            dict[row[index]] = {row[0]: 1}
    return

# Calculate average entropy (or information) for attribute
def calculateAverageEntropy( dict, sumEntries ):
    entropy = 0.0
    for key,value in dict.items():
        entropy += ( sum(value.values())/float(sumEntries) * information(value.values()) )
    return entropy

# Execution starts here
with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    # Place values into respective arrays
    for row in reader:
    # for i in range(0, 600000):
    #     row = reader.next()

        # Generate tables with support for each trip type
        generateAttributeTable(visitNumberDict, 1, row)
        generateAttributeTable(weekdayDict, 2, row)
        generateAttributeTable(upcDict, 3, row)
        generateAttributeTable(scanCountDict, 4, row)
        generateAttributeTable(departmentDescriptionDict, 5, row)
        generateAttributeTable(finelineNumberDict, 6, row)

    # Get sum of entries
    sumEntries = 0
    for key,value in visitNumberDict.items():
        for k,v in value.items():
            sumEntries += v

    # Calculate entropy
    visitNumberAE = calculateAverageEntropy(visitNumberDict, sumEntries)
    weekdayAE = calculateAverageEntropy(weekdayDict, sumEntries)
    upcAE = calculateAverageEntropy(upcDict, sumEntries)
    scanCountAE = calculateAverageEntropy(scanCountDict, sumEntries)
    departmentAE = calculateAverageEntropy(departmentDescriptionDict, sumEntries)
    finelineNumberAE = calculateAverageEntropy(finelineNumberDict, sumEntries)

    # Calculate information
    visitNumberEntropy = calculateEntropy(visitNumberDict)
    weekdayEntropy = calculateEntropy(weekdayDict)
    upcEntropy = calculateEntropy(upcDict)
    scanCountEntropy = calculateEntropy(scanCountDict)
    departmentEntropy = calculateEntropy(departmentDescriptionDict)
    finelineNumberEntropy = calculateEntropy(finelineNumberDict)

    # Calculate information gain
    visitNumberIG = visitNumberEntropy - visitNumberAE
    weekDayIG = weekdayEntropy - weekdayAE
    upcIG = upcEntropy - upcAE
    scanCountIG = scanCountEntropy - scanCountAE
    departmentIG = departmentEntropy - departmentAE
    finelineNumberIG = finelineNumberEntropy - finelineNumberAE

    print visitNumberIG
    print weekDayIG
    print upcIG
    print scanCountIG
    print departmentIG
    print finelineNumberIG

csvfile.close()
