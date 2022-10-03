from flask import Flask,session
from App.config import ApplicationConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_cors import CORS 


app = Flask(__name__)
app.config.from_object(ApplicationConfig)
bcrypt = Bcrypt(app)
server_session = Session(app)
CORS(app, supports_credentials=True)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from App import routes