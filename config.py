import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #Flask-WTF extension uses SECRET_KEY to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF