#clustering based on trip types

import csv
from math import pow, sqrt

TripType3 = []
TripType4 = []
TripType5 = []
TripType6 = []
TripType7 = []
TripType8 = []
TripType9 = []
TripType12 = []
TripType14 = []
TripType15 = []
TripType18 = []
TripType19 = []
TripType20 = []
TripType21 = []
TripType22 = []
TripType23 = []
TripType24 = []
TripType25 = []
TripType26 = []
TripType27 = []
TripType28 = []
TripType29 = []
TripType30 = []
TripType31 = []
TripType32 = []
TripType33 = []
TripType34 = []
TripType35 = []
TripType36 = []
TripType37 = []
TripType38 = []
TripType39 = []
TripType40 = []
TripType41 = []
TripType42 = []
TripType43 = []
TripType44 = []
TripType999 = []
#cluster each tripType into a list containing its data


#[0] = support (# rows total of this triptype)
#[1] = visits (# visits of this triptype -> divide into support to find
			   # avg number of rows PER visit)
#[2] = Average rows per visit of this triptype
#[3] = upc dictionary, key = upc #, value = quantity
#[4] = department dictionary, key = department, value = quantity
#[5] = fineline dictionary, key = fineline #, value = quantity


def create_training_data_cluster(List, tripType):
    with open('train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        attributes = reader.next()
        row = attributes
        upcDict = {}
        departmentDict = {}
        finelineDict = {}
        List.append(0)		#support
        List.append(0)		#visits
        for row in reader:
        #for i in range(0,10000):
        	prevRow = row
        	row = reader.next()

       		if (int(row[0]) == tripType):		#increment support if training triptype matches parameter	
	       		List[0] += 1 	     

	       		if (row[1] != prevRow[1]):		#increment visits if visit number changes
	       			List[1] += 1 				

	        	if row[3] in upcDict:			#for each dictionary, key = atrribute, value = count
	        		upcDict[row[3]] += int(row[4])
	        	else:
	        		upcDict[row[3]] = int(row[4])

	        	if row[5] in departmentDict:
	        		departmentDict[row[5]] += int(row[4])
	        	else:
	        		departmentDict[row[5]] = int(row[4])

	        	if row[6] in finelineDict:
	        		finelineDict[row[6]] += int(row[4])
	        	else:
	        		finelineDict[row[6]] = int(row[4])

	     

        AvgRows = float(List[0])/float(List[1])
        
        List.append(AvgRows)			#average rows per visit of that triptype
        List.append(upcDict)
        List.append(departmentDict)
        List.append(finelineDict)
    
    csvfile.close()
    return

create_training_data_cluster(TripType3, 3)
create_training_data_cluster(TripType4, 4)
create_training_data_cluster(TripType5, 5)
create_training_data_cluster(TripType6, 6)
create_training_data_cluster(TripType7, 7)
create_training_data_cluster(TripType8, 8)
create_training_data_cluster(TripType9, 9)
create_training_data_cluster(TripType12, 12)
create_training_data_cluster(TripType14, 14)
create_training_data_cluster(TripType15, 15)
create_training_data_cluster(TripType18, 18)
create_training_data_cluster(TripType19, 19)
create_training_data_cluster(TripType20, 20)
create_training_data_cluster(TripType21, 21)
create_training_data_cluster(TripType22, 22)
create_training_data_cluster(TripType23, 23)
create_training_data_cluster(TripType24, 24)
create_training_data_cluster(TripType25, 25)
create_training_data_cluster(TripType26, 26)
create_training_data_cluster(TripType27, 27)
create_training_data_cluster(TripType28, 28)
create_training_data_cluster(TripType29, 29)
create_training_data_cluster(TripType30, 30)
create_training_data_cluster(TripType31, 31)
create_training_data_cluster(TripType32, 32)
create_training_data_cluster(TripType33, 33)
create_training_data_cluster(TripType34, 34)
create_training_data_cluster(TripType35, 35)
create_training_data_cluster(TripType36, 36)
create_training_data_cluster(TripType37, 37)
create_training_data_cluster(TripType38, 38)
create_training_data_cluster(TripType39, 39)
create_training_data_cluster(TripType40, 40)
create_training_data_cluster(TripType41, 41)
create_training_data_cluster(TripType42, 42)
create_training_data_cluster(TripType43, 43)
create_training_data_cluster(TripType44, 44)
create_training_data_cluster(TripType999, 999)

print TripType26



	        	
