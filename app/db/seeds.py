from pymongo import MongoClient
import json

client = MongoClient('localhost:27017')
db = client.wikigraph
db.drop_collection('asian_american')

filename = "static/author_data.json"
with open(filename) as data_file:
    data = json.load(data_file)

db.asian_american.insert(data)

print("Seeded database with file {0}".format(filename))
