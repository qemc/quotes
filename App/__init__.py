from flask import Flask
from App.config import ApplicationConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(ApplicationConfig)
db = SQLAlchemy(app)

from App import routes