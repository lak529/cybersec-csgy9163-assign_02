from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app import app, models, db
from app.forms import LoginForm, RegistrationForm
from app.models import User



debug = True

@app.route('/')
@app.route('/index')
@login_required #force a login to view this page
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET','POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('index'))
    form = LoginForm()
    if(form.validate_on_submit()):
        #grab the user field, and perform a query by it, and grab the first result
        user = User.query.filter_by(username=form.username.data).first()
        #if we get no user (username mismatch) or password is wrong, say invalid
        if(user is None or not user.checkpw(form.password.data)):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        #reroute to origin
        next_page = request.args.get('next')
        if(not next_page or url_parse(next_page).netloc != ''):
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(current_user.is_authenticated):
        return redirect(url_for('index'))
    form = RegistrationForm()
    if(form.validate_on_submit()):
        user = User(username=form.username.data, email=form.email.data)
        user.setpw(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

