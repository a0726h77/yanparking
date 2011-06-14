# coding:utf-8

from lxml import etree
from squawk.query import *
from squawk.parsers.csvparser import *

parking_datastore_file = 'parking_20110605.xml'
# 從 http://iteamjob.appspot.com/rest/parking 保存

tpis_parking_file = 'tpis_parking.csv'
# 利用 gen_tpis_parking_list.py 建立

f = open('parking_key_list.py', 'w')
f.write('parking = {\n')

tree = etree.parse(open(parking_datastore_file, 'rb'))
root = tree.getroot()

for i in range(1, 181):
    if len(str(i)) == 1 :
        i='00'+str(i)
    if len(str(i)) == 2 :
        i='0'+str(i)

    source = CSVParser(tpis_parking_file)
    query = Query("SELECT name FROM file WHERE id='%s'" % i)
    name = [ row['name'] for row in query(source) ]

    if name:
        name = name[0]
        for child in root:
            #for son in child.iter():
            for son in child:
                if son.tag == 'name':
                    if son.text == name.decode('utf-8') :
                        e = (son.getparent())
                        f.write('\'%s\' : \'%s\',\n' % (i, e[0].text))
                        print '%s %s => %s' % (i, name, e[0].text)

                                               
f.write('}')
f.close()
