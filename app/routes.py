import os, json
from flask import render_template
from app import wikigraph

wikigraph.config.from_pyfile('config_file.cfg')

@wikigraph.route('/')
@wikigraph.route('/index')
def index():
    filename = os.path.join(wikigraph.static_folder, 'author_data.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return render_template("index.html", data=data, nyt_api_key=wikigraph.config['NYT_API_KEY'])
