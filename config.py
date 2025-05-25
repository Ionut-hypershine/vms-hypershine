import os

class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'your_username'
    MAIL_PASSWORD = 'your_password'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    UPLOAD_FOLDER = 'payslips'
