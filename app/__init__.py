from flask import Flask
from config import Config

wikigraph = Flask(__name__)
wikigraph.config.from_object(Config)

from app import routes
