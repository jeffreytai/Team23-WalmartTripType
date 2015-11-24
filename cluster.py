import csv
from math import pow, sqrt

trainDepartmentDict = {}
testDepartmentDict = {}
trainTripType = []
testTripType = []

# Paramters: 2 arrays
# Output: distance between two arrays, using Euclidean distance
def calculate_distance( arr1, arr2 ):
    distance = 0.0
    for i in range(0, len(arr1)):
        distance += pow((arr2[i] - arr1[i]), 2)
    return sqrt(distance)

# Each entry in the training data dictionary corresponds to one cluster of visits
# We include the support of all departments
# There are 95,674 total clusters
def create_training_data_dictionary():
    with open('train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        attributes = reader.next()

        # Place values into respective arrays
        for row in reader:
        # for i in range(0,100):
        #     row = reader.next()

            # null department??
            if row[1] in trainDepartmentDict:
                trainDepartmentDict[row[1]][row[5]] += int(row[4])
            else:
                trainTripType.append(row[0])
                trainDepartmentDict[row[1]] = {
                        'FINANCIAL SERVICES': 0,
                        'SHOES': 0,
                        'PERSONAL CARE': 0,
                        'PAINT AND ACCESSORIES': 0,
                        'DSD GROCERY': 0,
                        'MEAT - FRESH & FROZEN': 0,
                        'DAIRY': 0,
                        'PETS AND SUPPLIES': 0,
                        'HOUSEHOLD CHEMICALS/SUPP': 0,
                        'NULL': 0,
                        'IMPULSE MERCHANDISE': 0,
                        'PRODUCE': 0,
                        'CANDY, TOBACCO, COOKIES': 0,
                        'GROCERY DRY GOODS': 0,
                        'BOYS WEAR': 0,
                        'FABRICS AND CRAFTS': 0,
                        'JEWELRY AND SUNGLASSES': 0,
                        'MENS WEAR': 0,
                        'ACCESSORIES': 0,
                        'HOME MANAGEMENT': 0,
                        'FROZEN FOODS': 0,
                        'SERVICE DELI': 0,
                        'INFANT CONSUMABLE HARDLINES': 0,
                        'PRE PACKED DELI': 0,
                        'COOK AND DINE': 0,
                        'PHARMACY OTC': 0,
                        'LADIESWEAR': 0,
                        'COMM BREAD': 0,
                        'BAKERY': 0,
                        'HOUSEHOLD PAPER GOODS': 0,
                        'CELEBRATION': 0,
                        'HARDWARE': 0,
                        'BEAUTY': 0,
                        'AUTOMOTIVE': 0,
                        'BOOKS AND MAGAZINES': 0,
                        'SEAFOOD': 0,
                        'OFFICE SUPPLIES': 0,
                        'LAWN AND GARDEN': 0,
                        'SHEER HOSIERY': 0,
                        'WIRELESS': 0,
                        'BEDDING': 0,
                        'BATH AND SHOWER': 0,
                        'HORTICULTURE AND ACCESS': 0,
                        'HOME DECOR': 0,
                        'TOYS': 0,
                        'INFANT APPAREL': 0,
                        'LADIES SOCKS': 0,
                        'PLUS AND MATERNITY': 0,
                        'ELECTRONICS': 0,
                        'GIRLS WEAR, 4-6X  AND 7-14': 0,
                        'BRAS & SHAPEWEAR': 0,
                        'LIQUOR,WINE,BEER': 0,
                        'SLEEPWEAR/FOUNDATIONS': 0,
                        'CAMERAS AND SUPPLIES': 0,
                        'SPORTING GOODS': 0,
                        'PLAYERS AND ELECTRONICS': 0,
                        'PHARMACY RX': 0,
                        'MENSWEAR': 0,
                        'OPTICAL - FRAMES': 0,
                        'SWIMWEAR/OUTERWEAR': 0,
                        'OTHER DEPARTMENTS': 0,
                        'MEDIA AND GAMING': 0,
                        'FURNITURE': 0,
                        'OPTICAL - LENSES': 0,
                        'SEASONAL': 0,
                        'LARGE HOUSEHOLD GOODS': 0,
                        '1-HR PHOTO': 0,
                        'CONCEPT STORES': 0,
                        'HEALTH AND BEAUTY AIDS': 0
                    }
                trainDepartmentDict[row[1]][row[5]] = int(row[4])
    csvfile.close()
    return

# Each entry in the test data dictionary corresponds to one cluster of visits
# We include ONLY the departments (and their support) that appear in the visit
def create_testing_data_dictionary():
    with open('test.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        attributes = reader.next()

        # for row in reader:
        for i in range(0,100):
            row = reader.next()

            if row[0] in testDepartmentDict:
                if row[4] in testDepartmentDict[row[0]]:
                    testDepartmentDict[row[0]][row[4]] += int(row[3])
                else:
                    testDepartmentDict[row[0]][row[4]] = int(row[3])
            else:
                testDepartmentDict[row[0]] = {}
                testDepartmentDict[row[0]][row[4]] = int(row[3])
    csvfile.close()
    return

# Compare the relevant support of a visit's departments
def classify_trip_types():
    for visitNumber,testdept in testDepartmentDict.items():
        deptDistances = []
        i = 0
        for tripType,traindept in trainDepartmentDict.items():

            # Gets support for relevant departments
            correspondingDepts = { name: traindept[name] for name in testdept.keys() }

            # Places distance between each cluster into an array
            deptDistances.append( calculate_distance(testdept.values(), correspondingDepts.values()) )
        # print deptDistances

        # Finds index n of minimum distance (trip type is nth cluster)
        idx = deptDistances.index(min(deptDistances))
        testTripType.append(trainTripType[idx])
    return


create_training_data_dictionary()
create_testing_data_dictionary()
classify_trip_types()

print testTripType
