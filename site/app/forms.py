from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], id='uname')
    password = PasswordField('Password', validators=[DataRequired()], id='pword')
    mfacode = StringField('2FA Code', validators=[DataRequired()], id='2fa')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], id='uname')
    password = PasswordField('Password', validators=[DataRequired()], id='pword')
    #password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    mfaid = StringField('2FA ID', validators=[DataRequired()], id='2fa')
    submit = SubmitField('Register')
    
    #the pattern 'validate_[x]' adds a custom validate to the [x] field
    def validate_username(self, username):
        #check if the user already exists
        user = User.query.filter_by(username=username.data).first()
        if(user is not None):
            raise ValidationError('Please use a different username')

class SpellCheckForm(FlaskForm):
    textin = TextAreaField('Text to Check', id='inputtext')
    #textout = TextAreaField('Text Checked', id='textout')
    #misspelled = TextAreaField('Misspelled Words', id='misspelled')
    submit = SubmitField('Check Text')





