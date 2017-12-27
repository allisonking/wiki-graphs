import os, json
from flask import render_template, g
from app import wikigraph
from pymongo import MongoClient
from bson.json_util import dumps

# read configuration file
wikigraph.config.from_pyfile('config_file.cfg')

def get_db():
    """Opens a new database connection if there is none yet for the current app context"""
    if not hasattr(g, 'db'):
        client = get_connection()
        g.db = client.wikigraph
    return g.db

def get_connection():
    if not hasattr(g, 'client'):
        g.client = MongoClient('localhost:27017')
    return g.client

def get_authors():
    db = get_db()
    cursor = db.asian_american.find({})
    return dumps(cursor)

@wikigraph.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request"""
    if hasattr(g, 'client'):
        print('Closing database connection...')
        g.client.close()

@wikigraph.route('/')
@wikigraph.route('/index')
def index():
    #filename = os.path.join(wikigraph.static_folder, 'author_data.json')
    #with open(filename) as data_file:
    #    data = json.load(data_file)
    data = json.loads(get_authors())
    return render_template("index.html", data=data, nyt_api_key=wikigraph.config['NYT_API_KEY'])
