from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient("mongodb+srv://admin:admin@cluster0.2agz2qq.mongodb.net/")
db = client.pytech
students = db.students

# Display all documents in the collection
print("All documents in the collection:")
docs = students.find({})
for doc in docs:
    print(doc)

# Display a single document by student_id
print("\nSingle document by student_id:")
doc = students.find_one({"student_id": 1007})
print(doc)