from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luna'}
    list = [{'p1':{'user': 'a'}, 'p2': 'Some msg'},
            {'p1':{'user': 'b'}, 'p2': 'Another msg'}
    ]
    return render_template('index.html', title='Home', user=user, list=list)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
