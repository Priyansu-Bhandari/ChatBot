import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/chatbot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
