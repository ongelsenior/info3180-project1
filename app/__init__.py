from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:jello21@localhost/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views