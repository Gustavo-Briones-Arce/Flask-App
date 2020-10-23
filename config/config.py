import os

SECRET_KEY = '1234ewq'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath(os.getcwd())  + '/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
