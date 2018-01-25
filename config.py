import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key-hehe'
    NYT_API_KEY = os.environ.get('NYT_API_KEY') or 'nyt-api-here'
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'localhost:27017'
    TEMPLATES_AUTO_RELOAD = True
