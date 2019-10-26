import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # used by flask to init crypto, flask-wtf uses to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    
    #setup sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #setup app tools
    SPELLCHECK_TEMP_DIR = os.environ.get('SPELLCHECK_TEMPDIR') or os.path.join(basedir, 'temp')
    SPELLCHECK_BIN_DIR = os.environ.get('SPELLCHECK_BINDIR') or os.path.join(basedir, 'bin')
    SPELLCHECK_TOOL = os.environ.get('SPELLCHECK_TOOL') or os.path.join(SPELLCHECK_BIN_DIR, 'a.out')
    SPELLCHECK_WORDLIST = os.environ.get('SPELLCHECK_WORDLIST') or os.path.join(SPELLCHECK_BIN_DIR, 'wordlist.txt')
    



