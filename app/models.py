from app import db
from flask_sqlalchemy import SQLAlchemy

class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    message = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    picture=db.Column(db.LargeBinary)
    datejoined = db.Column(db.DateTime)
    
    def __init__(self, userid, username, fname, lname, age, message,gender,picture, datejoined):
        
            self.userid=userid
            self.username=username
            self.fname=fname.title()
            self.lname=lname.title()
            self.age=age
            self.message=message
            self.gender= gender.upper()
            self.picture=picture
            self.datejoined=datejoined

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
        
    def get_id(self):
        try:
            return unicode(self.userid)
        except NameError:
            return str(self.userid)  
    
    def __repr__(self):
        return '<User %r>' % (self.username)