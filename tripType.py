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
# Output: information
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

# Calculates information for entire attribute
def calculateAttributeInformation( dict ):
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

# Unused -- just shows an example of how generateAttributeTable is working
def generateVisitNumberTable( row ):
    if row[1] in visitNumberDict:
        if row[0] in visitNumberDict[row[1]]:
            visitNumberDict[row[1]][row[0]] += 1
        else:
            visitNumberDict[row[1]][row[0]] = 1
    else:
        visitNumberDict[row[1]] = {row[0]: 1}
    return

# Calculate entropy for attribute
def calculateEntropy( dict, sumEntries ):
    entropy = 0.0
    for key,value in dict.items():
        entropy += ( sum(value.values())/float(sumEntries) * information(value.values()) )
    return entropy


with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    # Place values into respective arrays
    for i in range(0, 100000):
        row = reader.next()

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
    visitNumberEntropy = calculateEntropy(visitNumberDict, sumEntries)
    weekdayEntropy = calculateEntropy(weekdayDict, sumEntries)
    upcEntropy = calculateEntropy(upcDict, sumEntries)
    scanCountEntropy = calculateEntropy(scanCountDict, sumEntries)
    departmentEntropy = calculateEntropy(departmentDescriptionDict, sumEntries)
    finelineNumberEntropy = calculateEntropy(finelineNumberDict, sumEntries)

    # Calculate information
    visitNumberInformation = calculateAttributeInformation(visitNumberDict)
    weekdayInformation = calculateAttributeInformation(weekdayDict)
    upcInformation = calculateAttributeInformation(upcDict)
    scanCountInformation = calculateAttributeInformation(scanCountDict)
    departmentInformation = calculateAttributeInformation(departmentDescriptionDict)
    finelineNumberInformation = calculateAttributeInformation(finelineNumberDict)

    # print visitNumberInformation
    # print weekdayInformation
    # print upcInformation
    # print scanCountInformation
    # print departmentInformation
    # print finelineNumberInformation

    visitNumberIG = visitNumberInformation - visitNumberEntropy
    weekDayIG = weekdayInformation - weekdayEntropy
    upcIG = upcInformation - upcEntropy
    scanCountIG = scanCountInformation - scanCountEntropy
    departmentIG = departmentInformation - departmentEntropy
    finelineNumberIG = finelineNumberInformation - finelineNumberEntropy

    print visitNumberIG
    print weekDayIG
    print upcIG
    print scanCountIG
    print departmentIG
    print finelineNumberIG


csvfile.close()
