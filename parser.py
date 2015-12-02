import csv
import sys

if(len(sys.argv) != 3):
	print("Error: input and output filenames must be specified")
	exit()

f = open(sys.argv[1], "r")
try:
	reader = csv.reader(f)
	for row in reader:
		b = row;
finally: f.close()

orig_len = len(b)
b[0] = b[0].replace("{", "")
b[len(b)-1] = b[len(b)-1].replace("}", "")


for num in range(0 , len(b)): 
	#remove 's and spaces
	temp = b[num].replace("'", "").replace(" ", "")
	b[num] = temp.split(":")
	b[num][0] = int(b[num][0]) 
	b[num][1] = int(b[num][1])
	#print b[num]

#sort transaction IDs
b = sorted(b,key=lambda b: (b[0],b[1]))


# 0 - 44 for 43 types and 1 transaction ID
row_orig = []
for num in range(0,44):
	row_orig.append('0')

with open(sys.argv[2], "wb") as csvfile:
	writer = csv.writer(csvfile, delimiter = ",")
	writer.writerow(['Visit_number', 'TripType_3', 'TripType_4', 'TripType_5', 'TripType_6'
		, 'TripType_7', 'TripType_8', 'TripType_9', 'TripType_12'
		, 'TripType_14', 'TripType_15', 'TripType_18'
		, 'TripType_19', 'TripType_20', 'TripType_21', 'TripType_22', 'TripType_23', 'TripType_24'
		, 'TripType_25', 'TripType_26', 'TripType_27', 'TripType_28', 'TripType_29', 'TripType_30'
		, 'TripType_31', 'TripType_32', 'TripType_33', 'TripType_34', 'TripType_35', 'TripType_36'
		, 'TripType_37', 'TripType_38', 'TripType_39', 'TripType_40', 'TripType_41', 'TripType_42'
		, 'TripType_43', 'TripType_44', 'TripType_999'])
	for num in range(0, orig_len):
		#assume 44 classes
		col = int(b[num][1])-2
		row_orig[0] = str(b[num][0])
		if(b[num][1] == 999):
			row_orig[43] = str(1)
		else:
			row_orig[col] = str(1)
		write_row = []
		write_row.append(row_orig[0])
		write_row.append(row_orig[1])
		write_row.append(row_orig[2])
		write_row.append(row_orig[3])
		write_row.append(row_orig[4])
		write_row.append(row_orig[5])
		write_row.append(row_orig[6])
		write_row.append(row_orig[7])
		write_row.append(row_orig[10])
		write_row.append(row_orig[12])
		write_row.append(row_orig[13])
		write_row.append(row_orig[16])
		write_row.append(row_orig[17])
		write_row.append(row_orig[18])
		write_row.append(row_orig[19])
		write_row.append(row_orig[20])
		write_row.append(row_orig[21])
		write_row.append(row_orig[22])
		write_row.append(row_orig[23])
		write_row.append(row_orig[24])
		write_row.append(row_orig[25])
		write_row.append(row_orig[26])
		write_row.append(row_orig[27])
		write_row.append(row_orig[28])
		write_row.append(row_orig[29])
		write_row.append(row_orig[30])
		write_row.append(row_orig[31])
		write_row.append(row_orig[32])
		write_row.append(row_orig[33])
		write_row.append(row_orig[34])
		write_row.append(row_orig[35])
		write_row.append(row_orig[36])
		write_row.append(row_orig[37])
		write_row.append(row_orig[38])
		write_row.append(row_orig[39])
		write_row.append(row_orig[40])
		write_row.append(row_orig[41])
		write_row.append(row_orig[42])
		write_row.append(row_orig[43])
		writer.writerow(write_row)
		if(b[num][1] == 999):
			row_orig[43] = str(0)
		else:
			row_orig[col] = str(0)
		


