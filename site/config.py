import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # used by flask to init crypto, flask-wtf uses to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    
    #setup sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    



