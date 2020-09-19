import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Material(db.Model):
    name = db.StringProperty(required = True)
    water_usage = db.IntegerProperty(required = True)
    energy_usage = db.IntegerProperty(required = True)
    emissions = db.IntegerProperty(required = True)
    score = db.IntegerProperty(required = True)


material = Material(name="Nylon",
                    water_usage = 3,
                    energy_usage = 3,
                    emissions = 4,
                    score = 10)


# sample query
mat_list = ["Nylon", "Cotton", "Wool"]
mat_score = db.GqlQuery("SELECT * FROM Material WHERE name IN :1", mat_list)
