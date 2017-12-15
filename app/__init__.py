from flask import Flask

wikigraph = Flask(__name__)

from app import routes
