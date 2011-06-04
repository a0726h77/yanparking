# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template

from model_parking import Parking

class MainPage(webapp.RequestHandler):
      def get(self):
          parking = db.get(self.request.get('k'))

          template_values = {
	      'name' : parking.name,
	      'space' : parking.space,
		  'price' : parking.price,
	      'address' : parking.address,
	      'k' : self.request.get('k')
           }

          path = os.path.join(os.path.dirname(__file__), 'parking_view.html')
          self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/parking_view', MainPage)],
                                          debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
