# coding:utf-8


import re
import urllib2
from parking_key_list import *




global id
global remain_space
id = []
remain_space = []




# 建立 id[], remain_space[]
for i in [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' ]:
    try:
        url = "http://www.tpis.nat.gov.tw/InternetPDA/park_text.asp?groupid=%s" % i
        results = urllib2.urlopen(url)

        count = 0
        for result in results:
            m = re.search('parkid=(.*)\', \'parkoneinformation.*onkeypress', result)
            if m:
                id.append(m.group(1))
                #print parking[id]
    
            n = re.search(r'.*<td align="center">(.*)</td>', result)
            if ((count %2) == 0) and n:
                remain_space.append(n.group(1))
                #print remain_space
            count += 1
    except urllib2.URLError, e:
        pass
#        handleError(e)




# 將 id[], remain_space[] 更新至 Datastore
for i,s in zip(id, remain_space):
    try:
        if parking[i]:
            print '更新 id:%s space:%s http://iteamjob.appspot.com/rest/parking/%s' % (i, s, parking[i])
            xml_data = "<parking><space>%s</space></parking>" % s
            request = urllib2.Request('http://iteamjob.appspot.com/rest/parking/%s' % parking[i], xml_data)
            urllib2.urlopen(request)
    except:
            print 'Datastore未建立 id %s 的資料 http://www.tpis.nat.gov.tw/Internet/showinformation.asp?id=%s' % (i, i) 

