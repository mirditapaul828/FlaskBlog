from flask import Flask  #Import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)       #Set app to an instance of flask
app.config['SECRET_KEY'] = '10760aebb0732e9d9083454f7604db15' #Create a secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #For development ONLY
db = SQLAlchemy(app) #With SQLAlchemy we can represent our database as classes, called models
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes