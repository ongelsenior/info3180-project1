from flask_wtf import Form
from wtforms import TextField, RadioField, DateField, FileField
from wtforms.validators import DataRequired, Required, InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired, DataRequired


class ProfileForm(Form):
  fname = TextField('fname', validators=[InputRequired()])
  lname = TextField('lname', validators=[InputRequired()])
  username = TextField('username', validators=[InputRequired()])
  age = DateField('age', format='%Y-%m-%d', validators=[DataRequired()])
  gender = RadioField('gender', choices=[('Male','Male'), ('Female', 'Female')], validators=[InputRequired()])
  message= TextField('message', validators=[InputRequired()])
  picture = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])



