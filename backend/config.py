import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://sarthak:sg123@localhost/investedge')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
