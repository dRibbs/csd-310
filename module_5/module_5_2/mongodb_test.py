#importing MongoClient
from pymongo import MongoClient

#Variable for my url
url = "mongodb+srv://admin:admin@cluster0.2agz2qq.mongodb.net/"

#variable for my client
client = MongoClient(url)

#variable for the pytech db
db = client.pytech

#print statement
print(db.list_collection_names())