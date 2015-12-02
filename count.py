import csv

upcDict = {}
finelineDict = {}
departmentDict = {}
upcCount = 0
finelineCount = 0
departmentCount = 0

with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    for row in reader:
        if row[3] not in upcDict:
            upcDict[row[3]] = 1
            upcCount += 1
        # if row[5] not in departmentDict:
        #     departmentDict.append(row[5])
        #     departmentCount += 1
        # if row[6] not in finelineDict:
        #     finelineDict[row[6]] = 1
        #     finelineCount += 1

csvfile.close()

print upcCount #97715
# print finelineCount #5196
# print departmentCount #69
