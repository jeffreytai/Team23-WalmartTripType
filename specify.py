import csv

with open('train.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  attributes = reader.next()

  f = open('triptype.txt', 'w')
  # Clears file before writing
  f.seek(0)
  f.truncate()
  for row in reader:
  # for i in range(0, 1000):
    #   row = reader.next()

      if row[0] == '28':
          f.write(str(row))
          f.write('\n')

  f.close()

csvfile.close()
