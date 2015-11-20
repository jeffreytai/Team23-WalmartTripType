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


with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    # Place values into respective arrays
    for i in range(0, 110):
        row = reader.next()

        # Generate tables with support for each trip type
        generateVisitNumberTable(row)
        generateDepartmentDescriptionTable(row)

    # Get sum of entries
    sumEntries = 0
    for key,value in visitNumberDict.items():
        for k,v in value.items():
            sumEntries += v
    print sumEntries

    # Calculate entropy
    entropy = 0.0
    for key,value in departmentDescriptionDict.items():
        entropy += ( sum(value.values())/float(sumEntries) * information(value.values()) )

    print entropy


    # print numEntries
    # print visitNumberDict
    print departmentDescriptionDict


csvfile.close()
