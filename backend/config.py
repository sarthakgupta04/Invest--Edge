import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sarthak:sg123@localhost/investedge'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
