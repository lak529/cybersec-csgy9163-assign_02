from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app import app, models, db
from app.forms import LoginForm, RegistrationForm, SpellCheckForm
from app.models import User
from app.utils import perform_spellcheck



debug = True

@app.route('/')
@app.route('/index')
@login_required #force a login to view this page
def index():
    return redirect(url_for('spell_check'))

@app.route('/login', methods=['GET','POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('index'))
    form = LoginForm()
    if(form.is_submitted()):
        if(form.validate()):
            #grab the user field, and perform a query by it, and grab the first result
            user = User.query.filter_by(username=form.username.data).first()
            #if we get no user (username mismatch) or password is wrong, say invalid
            if(user == None or not user.checkpw(form.password.data)):
                return render_template('login_results.html', title='Login Failed', form=form, results="Login failure: Incorrect username or password")
            if(not user.checkmfaid(form.mfacode.data)):
                return render_template('login_results.html', title='Login Failed', form=form, results="Login failure: Two-factor auth failure")
            login_user(user)
            return render_template('login_results.html', title='Login Success', form=form, results="Login success")
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(current_user.is_authenticated):
        return redirect(url_for('index'))
    form = RegistrationForm()
    if(form.is_submitted()):
        if(form.validate()):
            #test user existance
            uname = form.username.data
            pword = form.password.data
            mfaid = form.mfaid.data
            user = User.query.filter_by(username=uname).first()
            if(user != None):
                return render_template('register_results.html', title='Register Failed', form=form, results="Registration failure: username in use")
            user = User(username=uname, mfaid=mfaid)
            user.setpw(pword)
            db.session.add(user)
            db.session.commit()
            return render_template('register_results.html', title='Register Successful', form=form, results="Registration success")
        else:
            return render_template('register_results.html', title='Register Failed', form=form, results="Registration failure: invalid fields")
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
@login_required #force a login to view this page
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/spell_check', methods=['GET', 'POST'])
@login_required #force a login to view this page
def spell_check():
    form = SpellCheckForm()
    if(form.validate_on_submit()):
        textout = form.textin.data
        misspelled = []
        perform_spellcheck(form.textin.data, misspelled)
        return render_template('spellcheckout.html', title='Spell Check Results', form=form, textout=textout, misspelled=misspelled)
    return render_template('spellcheckin.html', title='Enter Text to Spell Check', form=form)
    
