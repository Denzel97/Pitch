from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    name = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
      
    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'{self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
   
class Pitch(db.Model):
    pitch_list=[]
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    post = db.Column(db.String(255), index = True)
    title = db.Column(db.String(255),index = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
 

    def __init__(self,title,post,user):
        self.user = user
        self.title = title
        self.post = post

    def save_pitch(self):
        '''
        Function that saves all pitches posted
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries database and returns all posted pitches.
        '''
        pitches = pitch.query.all()
        return pitches

    @classmethod
    def delete_all_pitches(cls):
        pitch.all_pitches.delete()
