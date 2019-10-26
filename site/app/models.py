from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    mfaid = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    
    def setpw(self, pw):
        self.password_hash = generate_password_hash(pw)
    
    def checkpw(self, pw):
        return check_password_hash(self.password_hash, pw)
    
    # self.ToString()
    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))







