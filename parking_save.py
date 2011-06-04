# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template

#from datetime import tzinfo, timedelta
from model_parking import Parking

#class TaiwanTimeZone(tzinfo):
#  def utcoffset(self, dt):
#    return timedelta(hours=8)

#  def tzname(self, dt):
#    return 'CST'
	
#  def dst(self, dt):
#    return timedelta(hours=0)
	
#datetime=datetime.datetime.now(TaiwanTimeZone())    

#datetime.put()  
#class Parking(db.Model):
    #total = db.StringProperty()
    #space = db.StringProperty()
    #price = db.StringProperty()
    #name = db.StringProperty()
    #address = db.StringProperty()
    #geopt = db.GeoPtProperty()
	#datetime = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def post(self):

        print self.request.get('name').encode('utf-8') + "<br>"
	
	if self.request.get('k'):
	    p = db.get(db.Key(self.request.get('k')))

	    p.name = self.request.get('name')
            p.address = self.request.get('address')
            p.geopt = db.GeoPt(self.request.get('lat'),self.request.get('lng'))
	    p.total = self.request.get('total')
	    p.space = self.request.get('space')
	    p.price = self.request.get('price')
		
            p.put()
            print "update success"
        else:
            p = Parking(name=self.request.get('name'),
			       total=self.request.get('total'),
				   space=self.request.get('space'),
                   price=self.request.get('price'),
				   detail=self.request.get('detail'),
				   address=self.request.get('address'),
                   geopt=db.GeoPt(self.request.get('lat'),self.request.get('lng')))
                   
            db.put(p)
            print "add success"

        print "<a href=\"/parking_add\">Add</a><br>"
        print "<a href=\"/\">View</a><br>"

application = webapp.WSGIApplication(
                                     [('/parking_save', MainPage)],
                                          debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
	

