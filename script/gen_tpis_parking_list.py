# coding:utf-8

import re
import urllib2
import time

f = open('tpis_parking.csv', 'w')

f.write('id,name\n')
f.write(',\n')

for i in range(1, 181):
    if len(str(i)) == 1 :
        i='00'+str(i)
    if len(str(i)) == 2 :
        i='0'+str(i)
    try:
        url = "http://www.tpis.nat.gov.tw/Internet/showinformation.asp?id=%s" % i
        result = urllib2.urlopen(url)
        for r in result:
            m = re.search('<tr><caption>(.*)</catpion></tr>', r)
            if m:
                name = m.group(1)
                f.write('%s,%s\n' % (i, name))
    except urllib2.URLError, e:
        print '%s,' % i
        #handleError(e)
