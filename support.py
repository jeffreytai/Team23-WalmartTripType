import csv
import random

visitToTrip = {}

GROCERY_RELATED_DEPT = ["GROCERY DRY GOODS", "SEAFOOD", "FROZEN FOODS", "SERVICE DELI", "DAIRY", "DSD GROCERY", "COMM BREAD", "PRODUCE", "PRE PACKED DELI", "MEAT - FRESH & FROZEN", "GROCERY DRY GOODS"]

def meets_confidence( visit, deptArr, minConf ):
    count = len(visit)
    conf = 0.0
    for entry in visit:
        for dept in deptArr:
            if entry[4] == dept:
                conf += 1

    if (float(conf)/count) < minConf:
        return False
    else:
        return True

def meets_confidence_if_contains( visit, word, minConf ):
    count = len(visit)
    conf = 0.0
    for entry in visit:
        if word in entry[4]:
            conf += 1

    if (float(conf)/count) < minConf:
        return False
    else:
        return True


def classify( visit ):
    support = len(visit)

    if support <= 10:

        if meets_confidence(visit, ["FINANCIAL SERVICES"], 0.5):
            visitToTrip[visit[0][0]] = 3
            return

        if meets_confidence(visit, ["LIQUOR,WINE,BEER", "CANDY, TOBACCO, COOKIES"], 0.5):
            visitToTrip[visit[0][0]] = 6
            return

        if meets_confidence(visit, ["PHARMACY RX"], 1.0):
            emptyUTC = True
            # Checks for empty UTC number
            for entry in visit:
                if entry[2] != '':
                    emptyUTC = False

            if emptyUTC:
                visitToTrip[visit[0][0]] = 5
                return

        if meets_confidence(visit, ["PHARMACY OTC"], 0.5):
            # Ambiguous between TripType 4 and 5 in this case
            visitToTrip[visit[0][0]] = random.sample([4,5], 1)[0]
            return

        if support >= 4:
            if meets_confidence(visit, GROCERY_RELATED_DEPT, 0.5):
                visitToTrip[visit[0][0]] = 7
                return
        elif (support >= 1) and (support <= 3):
            if meets_confidence(visit, GROCERY_RELATED_DEPT, 0.5):
                visitToTrip[visit[0][0]] = 8
                return
            else:
                visitToTrip[visit[0][0]] = 9
                return

        if meets_confidence(visit, ["MEDIA AND GAMING"], 0.33):
            visitToTrip[visit[0][0]] = 23
            return

        if meets_confidence(visit, ["ELECTRONICS", "MEDIA AND GAMING"], 0.20):
            visitToTrip[visit[0][0]] = 22
            return

        if meets_confidence(visit, ["COOK AND DINE"], 0.25):
            visitToTrip[visit[0][0]] = 24
            return

        if meets_confidence(visit, ["HARDWARE"], 0.25):
            visitToTrip[visit[0][0]] = 26
            return

        if meets_confidence(visit, ["WIRELESS"], 0.25):
            visitToTrip[visit[0][0]] = 31
            return

        if meets_confidence(visit, ["DSD GROCERY"], 0.25):
            visitToTrip[visit[0][0]] = 35
            return

        if meets_confidence(visit, ["HOUSEHOLD PAPER GOODS"], 0.50):
            visitToTrip[visit[0][0]] = random.sample([12,14], 1)[0]
            return

        if meets_confidence(visit, ["CELEBRATION", "GROCERY DRY GOODS"], 0.25):
            visitToTrip[visit[0][0]] = 15
            return

        # Has no relation
        visitToTrip[visit[0][0]] = random.sample([43,999], 1)[0]
        return

    elif support <= 20:

        if meets_confidence(visit, ["HOUSEHOLD PAPER GOODS"], 0.50):
            visitToTrip[visit[0][0]] = random.sample([12,14], 1)[0]
            return

        if meets_confidence(visit, ["CELEBRATION", "GROCERY DRY GOODS"], 0.25):
            visitToTrip[visit[0][0]] = 15
            return

        if meets_confidence(visit, ["TOYS"], 0.25):
            visitToTrip[visit[0][0]] = 18
            return

        if meets_confidence(visit, ["ELECTRONICS"], 0.25):
            visitToTrip[visit[0][0]] = 19
            return

        if meets_confidence(visit, ["AUTOMOTIVE"], 0.25):
            visitToTrip[visit[0][0]] = 20
            return

        if meets_confidence(visit, ["OFFICE SUPPLIES", "FABRICS AND CRAFTS"], 0.50):
            visitToTrip[visit[0][0]] = 21
            return

        if meets_confidence_if_contains(visit, "WEAR", 0.50):
            visitToTrip[visit[0][0]] = 25
            return

        if meets_confidence(visit, ["HORTICULTURE AND ACCESS", "LAWN AND GARDEN"], 0.50):
            visitToTrip[visit[0][0]] = 27
            return

        if meets_confidence(visit, ["DSD GROCERY"], 0.25):
            visitToTrip[visit[0][0]] = 38
            return

        if meets_confidence(visit, GROCERY_RELATED_DEPT, 0.80):
            visitToTrip[visit[0][0]] = 39
            return

        # Assign to a miscellaneos triptype or 999
        visitToTrip[visit[0][0]] = random.sample([29,30,41,42,999], 1)[0]

    else:
        # No limit on size

        if meets_confidence(visit, ["SPORTING GOODS"], 0.50):
            visitToTrip[visit[0][0]] = 28
            return

        if meets_confidence(visit, ["INFANT CONSUMABLE HARDLINES"], 0.25):
            visitToTrip[visit[0][0]] = 32
            return

        if meets_confidence_if_contains(visit, "HOUSEHOLD", 0.50):
            visitToTrip[visit[0][0]] = 33
            return

        if meets_confidence(visit, ["PETS AND SUPPLIES"], 0.25):
            visitToTrip[visit[0][0]] = 34
            return

        if meets_confidence(visit, ["PERSONAL CARE"], 0.25):
            visitToTrip[visit[0][0]] = 36
            return

        if meets_confidence(visit, GROCERY_RELATED_DEPT, 0.50):
            visitToTrip[visit[0][0]] = 37
            return

        if meets_confidence_if_contains(visit, "GROCERY", 0.25):
            visitToTrip[visit[0][0]] = 40
            return

        # Not related
        visitToTrip[visit[0][0]] = random.sample([44,999], 1)[0]
        return


with open('test.csv', 'rb') as testfile:
    reader = csv.reader(testfile, delimiter=',', quotechar='"')
    attributes = reader.next()

    currentVisit = []
    for row in reader:
    # for i in range(0, 100):
        # row = reader.next()

        if (len(currentVisit) == 0) or (row[0] == currentVisit[0][0]):
            currentVisit.append(row)
        else:
            # Classify previous current visit
            classify(currentVisit)

            # Reset current visit then append
            currentVisit = []
            currentVisit.append(row)


testfile.close()


print visitToTrip
