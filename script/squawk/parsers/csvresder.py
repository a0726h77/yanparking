
import csv

fp = open('test.csv', "rb")
reader = csv.DictReader(fp, skipinitialspace=True)
print reader.next()
#headers = reader.fieldnames
#print headers
#reader = csv.reader(fp, delimiter=',')
columns = [x.lower() for x in reader.fieldnames]

print reader.fieldnames

for x in reader:
    print x

def __iter__():
    for row in self.reader:
        yield dict((k.lower(), v) for k, v in row.items())
