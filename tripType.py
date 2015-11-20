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

# Creates a dictionary of dictionaries
# Dictionary is a key-value pair of each unique visit number to a subdictionary
# Subdictionary contains key-value pairs of the TripType to its support
def generateVisitNumberTable( row ):
    if row[1] in visitNumberDict:
        if row[0] in visitNumberDict[row[1]]:
            visitNumberDict[row[1]][row[0]] += 1
        else:
            visitNumberDict[row[1]][row[0]] = 1
    else:
        visitNumberDict[row[1]] = {row[0]: 1}
    return

# Same as function above -- for weekday
def generateWeekdayTable( row ):
    if row[2] in weekdayDict:
        if row[0] in weekdayDict[row[2]]:
            weekdayDict[row[2]][row[0]] += 1
        else:
            weekdayDict[row[2]][row[0]] = 1
    else:
        weekdayDict[row[2]] = {row[0]: 1}
    return

# Same as function above -- for upc
# Upc might be empty
def generateUpcTable( row ):
    if row[3] != '':
        if row[3] in upcDict:
            if row[0] in upcDict[row[3]]:
                upcDict[row[3]][row[0]] += 1
            else:
                upcDict[row[3]][row[0]] = 1
        else:
            upcDict[row[3]] = {row[0]: 1}
    return

# Same as function above -- for scan count
def generateScanCountTable( row ):
    if row[4] in scanCountDict:
        if row[0] in scanCountDict[row[4]]:
            scanCountDict[row[4]][row[0]] += 1
        else:
            scanCountDict[row[4]][row[0]] = 1
    else:
        scanCountDict[row[4]] = {row[0]: 1}
    return

# Same as function above -- for department description
def generateDepartmentDescriptionTable( row ):
    if row[5] in departmentDescriptionDict:
        if row[0] in departmentDescriptionDict[row[5]]:
            departmentDescriptionDict[row[5]][row[0]] += 1
        else:
            departmentDescriptionDict[row[5]][row[0]] = 1
    else:
        departmentDescriptionDict[row[5]] = {row[0]: 1}
    return

# Same as function above -- for fineline number
def generateFinelineNumberTable( row ):
    if row[6] in finelineNumberDict:
        if row[0] in finelineNumberDict[row[6]]:
            finelineNumberDict[row[6]][row[0]] += 1
        else:
            finelineNumberDict[row[6]][row[0]] = 1
    else:
        finelineNumberDict[row[6]] = {row[0]: 1}
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
    for i in range(0, 50):
        row = reader.next()

        # Generate tables with support for each trip type
        generateVisitNumberTable(row)
        generateWeekdayTable(row)
        generateUpcTable(row)
        generateScanCountTable(row)
        generateDepartmentDescriptionTable(row)
        generateFinelineNumberTable(row)

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

    # print visitNumberEntropy
    # print weekdayEntropy
    # print upcEntropy
    # print scanCountEntropy
    # print departmentEntropy
    # print finelineNumberEntropy

csvfile.close()
