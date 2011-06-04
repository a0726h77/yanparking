# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template
import random
import re
import wsgiref.handlers

from model_parking import Parking

class MainPage(webapp.RequestHandler):
    def get(self):
        # Nearest records by latitude / longitude in SQL
	lat = float(self.request.get('lat', default_value="25.036004"))
	lon = float(self.request.get('lon', default_value="121.56720799999994"))
        #lat = float(25.036004)
        #lon = float(121.56720799999994)
        area = .004
        #area = .0005
        #area = .04
        minLat = lat - area
        minLon = lon - area
        maxLat = lat + area
        maxLon = lon + area
        query = db.GqlQuery("SELECT * FROM Parking WHERE geopt >= :1 AND geopt <= :2",db.GeoPt(lat=minLat, lon=minLon), db.GeoPt(lat=maxLat, lon=maxLon) )
        #query = db.GqlQuery("SELECT * FROM Parking")

        parkings = query.fetch(100)
        
        # 為使用者選出三筆
        #XXX 為使用者選出三筆, 目前為實驗所以先找空位大於40的 (可能在距離、價格、空位、我的最愛上做考量)
        _avalibal_parkings = list()
        for p in parkings:
            #XXX if re.sub('[a-zA-z-/.,=-]', '0', p.space) > 40:
            #XXX      _avalibal_parkings.append(p)
            _avalibal_parkings.append(p)
	if len(_avalibal_parkings) > 2 :
            three_parkings = random.sample(_avalibal_parkings, 3)
	else :
            three_parkings = _avalibal_parkings

        template_values = {
	    'lat' : lat,
	    'lon' : lon,
            'parkings' : parkings,
            'three_parkings' : three_parkings
            }

        path = os.path.join(os.path.dirname(__file__), 'geo_index.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/.*', MainPage)],
                                          debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

