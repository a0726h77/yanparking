# coding:utf-8


import re
import urllib2
from google.appengine.ext import db
from model_parking import Parking
#import time




# 停管處停車場 id 與 iteamjob 的 停車場 key 對應
parking = {
'001' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix5AMM',
'002' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp-wMM',
'003' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ7AMM',
'004' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjRgwQM',
'005' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5iwQM',
'006' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiC9AMM',
'007' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihkwQM',
'008' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiqvQMM',
'009' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJmwQM',
'010' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxogQM',
'011' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZqgQM',
'012' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjbrQMM',
'013' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiikwQM',
'014' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBsgQM',
'015' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxipugQM',
'016' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRwgQM',
'017' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5yQQM',
'018' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjh0QQM',
'019' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjJ2QQM',
'020' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix4QQM',
'021' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ6QQM',
'022' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB8QQM',
'023' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp-AQM',
'024' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjRgAUM',
'025' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5iAUM',
'026' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJmAUM',
'027' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJmAUM',
'028' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxnwUM',
'029' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZpwUM',
'030' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBrwUM',
'031' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjyogQM',
'032' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjq-wMM',
'033' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiC7gUM',
'034' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi6iwQM',
'035' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxia6QQM',
'036' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5hQYM',
'037' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjShgMM',
'038' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi6jgMM',
'039' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiy3gUM',
'040' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZpAYM',
'041' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBrAYM',
'042' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxia7AMM',
'043' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiptAYM',
'044' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRvAYM',
'045' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxib6QQM',
'048' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ4wYM',
'049' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp8gYM',
'051' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5ggcM',
'052' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihigcM',
'053' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxmQcM',
'054' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZoQcM',
'055' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjhyAcM',
'056' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB6AcM',
'057' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBpggM',
'058' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj6vQgM',
'059' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihhAkM',
'060' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjjyAcM',
'061' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxia4AcM',
'062' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZmwkM',
'063' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBowkM',
'064' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxipqwkM',
'065' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjT9wcM',
'066' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRswkM',
'067' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5ugkM',
'068' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjhwgkM',
'069' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjJygkM',
'070' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj6wAcM',
'071' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix0gkM',
'072' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ2gkM',
'073' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjanggM',
'074' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB4gkM',
'075' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp6QkM',
'076' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiqsQcM',
'077' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjR8QkM',
'078' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5-QkM',
'079' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihgQoM',
'080' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxkAoM',
'081' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZmAoM',
'082' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRsAoM',
'083' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjhvwoM',
'084' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjixQgM',
'085' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ1woM',
'086' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB3woM',
'087' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjR7goM',
'088' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj7vQgM',
'089' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp5goM',
'090' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjCoAoM',
'091' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjykAoM',
'092' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxixzwoM',
'093' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjJxwoM',
'094' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5twoM',
'095' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi7ggcM',
'096' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxipqAoM',
'097' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBoAoM',
'098' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi6_wcM',
'099' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiihwgM',
'100' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJiQoM',
'101' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ5gUM',
'102' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB7gUM',
'103' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp9QUM',
'105' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjR_QUM',
'109' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihjQYM',
'110' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjizgUM',
'113' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJlQYM',
'114' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxnAYM',
'115' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5wwYM',
'116' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB6wYM',
'117' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJkgcM',
'118' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjBqQcM',
'124' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxipsQcM',
'125' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxixzAsM',
'126' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRuQcM',
'127' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ1AsM',
'128' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxia1AsM',
'129' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB3AsM',
'130' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiC3AsM',
'131' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5wAcM',
'132' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjJ0AcM',
'133' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix2AcM',
'134' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ4AcM',
'135' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp7wcM',
'136' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjR9wcM',
'137' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5_wcM',
'138' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiy2AcM',
'139' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxia4wYM',
'140' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihhwgM',
'141' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJjwgM',
'142' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxlggM',
'149' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjaoQcM',
'150' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp4wsM',
'152' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZnggM',
'153' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiprggM',
'156' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjR6wsM',
'158' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRtggM',
'159' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5vQgM',
'160' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjS9wcM',
'161' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjhxQgM',
'162' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiC6AcM',
'163' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjq4wsM',
'164' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix1QgM',
'165' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjq_gIM',
'173' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi58wsM',
'176' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxih-wsM',
'177' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjr4wsM',
'178' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiD3AsM',
}




global id
global remain_space
id = []
remain_space = []




# 爬取停管處資訊, 建立 id[]、remain_space[]
try:
    url = "http://www.tpis.nat.gov.tw/Internet/park_text.asp"
    results = urllib2.urlopen(url)

    count = 0
    for result in results:
        m = re.search('parkid=(.*)\', \'parkoneinformation.*onkeypress', result)
        if m:
            id.append(m.group(1))
            #print m.group(1)#parking
            count = 0

        n = re.search(r'\s*<td align="center">(<font color="red">)*((\d{0,5})|(--)|(車位已滿)|(關閉))(</font>)*</td>\s*', result)
        if ((count %2) == 0) and n:
            remain_space.append(n.group(2))
            #print n.group(2)#remain_space
        count += 1
except urllib2.URLError, e:
    pass
    #handleError(e)




# 將 id[]、remain_space[] 更新至 Datastore
for i, s in zip(id, remain_space):
    try:
        if parking[i]:
            #print '更新 id:%s space:%s http://iteamjob.appspot.com/rest/parking/%s' % (i, s, parking[i])

	    # 使用 REST API 更新
            #xml_data = "<parking><space>%s</space></parking>" % s.decode('utf-8')
            #request = urllib2.Request('http://iteamjob.appspot.com/rest/parking/%s' % parking[i], xml_data)
            #urllib2.urlopen(request)
	    #time.sleep(0.5)

	    # 使用 Datastore 更新
	    p = db.get(db.Key(parking[i]))
	    p.space = s.decode('utf-8')
            p.put()
    except:
	#print 'Datastore未建立 id %s 的資料 http://www.tpis.nat.gov.tw/Internet/showinformation.asp?id=%s' % (i, i) 
        pass

