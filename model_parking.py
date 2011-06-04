from google.appengine.ext import db

class Parking(db.Model) :
  total = db.StringProperty()
  space = db.StringProperty()
  price = db.StringProperty()
  detail = db.StringProperty()
  address = db.StringProperty()
  name = db.StringProperty()
  geopt = db.GeoPtProperty(required=True)
  datetime = db.DateTimeProperty(auto_now=True)
  wait = db.StringProperty()
