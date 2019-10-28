from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import string
from flask_login import UserMixin
from app import db
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    mfaid = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    password_salt = db.Column(db.String(8)) #Luna 2019/10/27 improving security
    
    def setpw(self, pw):
        salt = ''.join(secrets.choice(string.ascii_letters+string.digits) for i in range(8))
        self.password_hash = generate_password_hash(salt+pw)
        self.password_salt = salt
    
    def checkpw(self, pw):
        return check_password_hash(self.password_hash, self.password_salt+pw)
    
    def checkmfaid(self, mid):
        #print(self.mfaid+":"+mid)
        return (self.mfaid==mid)
    
    # self.ToString()
    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))







