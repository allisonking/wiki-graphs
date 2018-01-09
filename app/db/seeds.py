from pymongo import MongoClient
from datetime import datetime
import json, os

client = MongoClient(os.environ.get('MONGODB_URI'))
db = client.wikigraph
#db.drop_collection('asian_american')

filename = "app/static/author_data.json"
with open(filename) as data_file:
    data = json.load(data_file)

data_in_one = {
"created_at": datetime.now(),
"data" : data
}

db.asian_american.insert(data_in_one)

print("Seeded database with file {0}".format(filename))
