import os, json
from flask import render_template, g, flash, redirect, url_for, request
from app import wikigraph
from pymongo import MongoClient
from bson.json_util import dumps, loads
from datetime import datetime

# read configuration file
wikigraph.config.from_pyfile('config_file.cfg')
MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = 'localhost:27017'

def get_db():
    """Opens a new database connection if there is none yet for the current app context"""
    if not hasattr(g, 'db'):
        client = get_connection()
        g.db = client.wikigraph
    return g.db

def get_connection():
    if not hasattr(g, 'client'):
        g.client = MongoClient(MONGO_URL)
    return g.client

def get_authors():
    db = get_db()
    cursor = db.asian_american.find().sort([('created_at', -1)]).limit(1)
    return dumps(cursor)

@wikigraph.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    payload = request.data
    data_in_one = {
    "created_at": datetime.now(),
    "data" : loads(payload)
    }
    db.asian_american.insert(data_in_one)
    flash('New entry was successfully posted')
    return redirect(url_for('index'))

@wikigraph.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request"""
    if hasattr(g, 'client'):
        print('Closing database connection...')
        g.client.close()

@wikigraph.route('/')
@wikigraph.route('/index')
def index():
    data = json.loads(get_authors())[0]['data']
    return render_template("index.html",
data=data,
data_subject="Asian American Literature",
nyt_api_key=wikigraph.config['NYT_API_KEY'],)
