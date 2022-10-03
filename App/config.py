

class ApplicationConfig():

    SECRET_KEY = '6be575743c714c0250e548de'
    
    SQLALCHEMY_DATABASE_URI =  'sqlite:///db.db'    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True