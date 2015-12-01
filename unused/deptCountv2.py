import csv

trainingDict = {}
productsDict = {}
mostFrequentDept = {}
averageProducts = {}

testDict = {}
testProductsDict = {}
testFrequentDept = {}
testAverageProducts = {}

visitToTrip = {}

with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    for row in reader:
    # for i in range(0, 1000):
        # row = reader.next()

        # Used for finding department with greatest support
        if row[0] in trainingDict:
            if row[5] in trainingDict[row[0]]:
                trainingDict[row[0]][row[5]] += int(row[4])
            else:
                trainingDict[row[0]][row[5]] = int(row[4])
        else:
            trainingDict[row[0]] = {}
            trainingDict[row[0]][row[5]] = int(row[4])

        # Used for finding average number of products purchased per visit
        if row[0] in productsDict:
            if row[1] in productsDict[row[0]]:
                productsDict[row[0]][row[1]] += int(row[4])
            else:
                # productsDict[row[0]]['visitCount'] += 1
                productsDict[row[0]][row[1]] = int(row[4])
        else:
            productsDict[row[0]] = {}
            # productsDict[row[0]]['visitCount'] = 1
            productsDict[row[0]][row[1]] = int(row[4])

csvfile.close()

# Iterates through training dictionary and finds most frequent department w/ count
# {'TripType': 'Department'}
for triptype,departments in trainingDict.items():
    dept = max(departments.iterkeys(), key=(lambda key: departments[key]))
    mostFrequentDept[triptype] = dept
    # mostFrequentDept[triptype] = {'dept': dept, 'count': trainingDict[triptype][dept]}

# Iterates through product dictionary and finds average products per visit for each trip type
# {'TripType': # Average Products}
for triptype,products in productsDict.items():
    numVisits = len(products)
    numProducts = sum(products.values())
    avgProducts = float(numProducts) / numVisits
    averageProducts[triptype] = avgProducts

print mostFrequentDept
# print averageProducts


with open('test.csv', 'rb') as testfile:
    reader = csv.reader(testfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    # Used for finding department with greatest support
    for row in reader:
    # for i in range(0, 100):
        # row = reader.next()

        if row[0] in testDict:
            if row[4] in testDict[row[0]]:
                testDict[row[0]][row[4]] += int(row[3])
            else:
                testDict[row[0]][row[4]] = int(row[3])
        else:
            testDict[row[0]] = {}
            testDict[row[0]][row[4]] = int(row[3])

        # Used for finding average number of products purchased per visits
        if row[0] in testProductsDict:
            testProductsDict[row[0]] += int(row[3])
        else:
            testProductsDict[row[0]] = int(row[3])

testfile.close()

# Iterates through test dictionary and finds most frequent department w/ count
for visitnumber,departments in testDict.items():
    dept = max(departments.iterkeys(), key=(lambda key: departments[key]))
    testFrequentDept[visitnumber] = dept

for visitnumber,department in testFrequentDept.items():
    candidates = []
    for triptype,dept in mostFrequentDept.items():
        if department == dept:
            candidates.append(triptype)

    # If there are multiple matching departments, find the one with the closest average products per visit
    if len(candidates) > 1:
        averageProductsForVisit = testProductsDict[visitnumber]
        avg = [(x,averageProducts[x]) for x in candidates]
        nearest = min([val[1] for val in avg], key=lambda x:abs(x-averageProductsForVisit))
        trip = [k for (k,v) in avg if v == nearest]
        visitToTrip[visitnumber] = trip[0]
    # If no matching candidates, trip type is 999
    elif len(candidates) == 0:
        visitToTrip[visitnumber] = '999'
    else:
        visitToTrip[visitnumber] = candidates[0]

# print visitToTrip
