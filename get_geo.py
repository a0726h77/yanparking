# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template
import os
import cgi


class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'get_geo.html')
        self.response.out.write(template.render(path, []))

application = webapp.WSGIApplication(
                                     [('/.*', MainPage)],
                                          debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

