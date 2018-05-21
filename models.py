from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy(app)

class FoodList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	location = db.Column(db.String(120), unique=True)
	weather = db.Column(db.String(20))
	
	def __init__(self, name, location, weather):
		self.name = name
		self.location = location
		self.weather = weather

	def __repr__(self):
		return '<Name %r>' % self.name