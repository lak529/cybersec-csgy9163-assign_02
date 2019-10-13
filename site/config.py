import os

class Config(object):
    # used by flask to init crypto, flask-wtf uses to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'

