import csv

trainDepartmentDict = {}

with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    for row in reader:
    # for i in range(0, 10):
    #     row = reader.next()

        if row[0] in trainDepartmentDict:
            if row[5] in trainDepartmentDict[row[0]]:
                trainDepartmentDict[row[0]][row[5]] += int(row[4])
            else:
                trainDepartmentDict[row[0]][row[5]] = int(row[4])
        else:
            trainDepartmentDict[row[0]] = {}
            trainDepartmentDict[row[0]][row[5]] = int(row[4])

csvfile.close()

print trainDepartmentDict
