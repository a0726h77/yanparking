# coding:utf-8

import re
import urllib2

global name
global space

parking = {
	'府前廣場地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix5AMM',
	'松壽公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp-wMM',
	'臺北市災害應變中心地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ7AMM',
	'雅祥公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjRgwQM',
	'世貿三館停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiC9AMM',
	'萬華國中地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxihkwQM',
	'君悅大飯店地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiqvQMM',
	'台北世貿中心展覽大樓地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiJmwQM',
	'台北國際會議中心地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjZqgQM',
	'台北世貿中心國貿大樓地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjxogQM',
	'附中公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjyogQM',
	'威秀影城松壽20' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjbrQMM',
	'威秀影城松壽18' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiikwQM',
	'立農公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5iwQM',
	'峨嵋立體停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxipugQM',
	'中山堂地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiRwgQM',
	'洛陽綜合立體停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjh0QQM',
	'光復北路立體停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxj5yQQM',
	'塔城公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjJ2QQM',
	'百齡高中地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxix4QQM',
	'前港公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiZ6QQM',
	'中坡公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxiB8QQM',
	'民權公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjp-AQM',
	'金華公園地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxjRgAUM',
	'古亭國中地下停車場' : 'aghpdGVhbWpvYnIPCxIHUGFya2luZxi5iAUM',
}
for i in range(1,200):
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
    
            m = re.search('<th>剩餘車位數：</th><td>(.*)</td>', r)
            if m:
                space = m.group(1)
    
        xml_data = "<parking><space>%s</space></parking>" % space
        request = urllib2.Request('http://yanparking.appspot.com/rest/parking/%s' % parking[name], xml_data)
        urllib2.urlopen(request)
    except urllib2.URLError, e:
        handleError(e)


