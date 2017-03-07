from flask.ext.wtf import Form
<<<<<<< HEAD
from flask.ext.uploads import *
from wtforms import TextField, RadioField, DateField, FileField
from wtforms.validators import DataRequired, Required, InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired


class Profile(Form):
  fname = TextField('fname', validators=[InputRequired()])
  lname = TextField('lname', validators=[InputRequired()])
  username = TextField('username', validators=[InputRequired()])
  sex = RadioField('Sex', choices=[('Male','Male'), ('Female', 'Female')], validators=[InputRequired()])
  age = DateField('age', format='%Y-%m-%d', validators=[DataRequired()])
  image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
                                         
=======
from wtforms.fields import TextField
# other fields include PasswordField
from wtforms.validators import required

class UserForm(Form):
  fisrt_name = TextField('first_name', validators=[required()])
  last_name = TextField('last_name', validators=[required()])
  age = TextField('age', validators=[required()])
  sex = TextField('sex', validators=[required()])
  image = TextField('image', validators=[required()])
