from flask.ext.wtf import Form

from flask.ext.uploads import *
from wtforms import TextField, RadioField, DateField, FileField
from wtforms.validators import DataRequired, Required, InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired


class Profile(Form):
  fname = TextField('fname', validators=[InputRequired()])
  lname = TextField('lname', validators=[InputRequired()])
  username = TextField('username', validators=[InputRequired()])
  age = DateField('age', format='%Y-%m-%d', validators=[DataRequired()])
  gender = RadioField('gender', choices=[('Male','Male'), ('Female', 'Female')], validators=[InputRequired()])
  message= TextField('message', validators=[InputRequired()])
  image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
                                         
=======
from wtforms.fields import TextField
# other fields include PasswordField
from wtforms.validators import required

class UserForm(Form):
  fisrt_name = TextField('first_name', validators=[required()])
  last_name = TextField('last_name', validators=[required()])
  age = TextField('age', validators=[required()])
  gender = TextField('gender', validators=[required()])
  message= TextField('message', validators=[required()])
  image = TextField('image', validators=[required()])
