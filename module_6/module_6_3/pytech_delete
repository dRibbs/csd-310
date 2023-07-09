# Gillenwater, Sam
# CYBR410 - Prof Haas

# MongoDB Student Data Management

# This script connects to a MongoDB database and performs operations on a collection named 'students'.
# It retrieves all documents from the collection, inserts a new document, deletes a specific document, and displays the updated collection.

# Prerequisites:
# - pymongo library must be installed (install via 'pip install pymongo')

# Instructions:
# 1. Ensure you have the necessary MongoDB connection string.
# 2. Update the connection string in the 'client' variable to point to your MongoDB cluster.
# 3. Run the script and observe the output.

# Note: This code assumes you have a MongoDB collection named 'students' with appropriate documents.

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

# Insert a new document with student_id 1010
student = {"student_id": 1010, "first_name": "Kyrie", "last_name": "Irving"}
students.insert_one(student)

# Display the inserted document
print("\nInserted document with student_id 1010:")
doc = students.find_one({"student_id": 1010})
print(doc)

# Delete the document with student_id 1010
students.delete_one({"student_id": 1010})
print("\nDocument with student_id 1010 deleted.")

# Display all documents in the collection after deletion
print("\nAll documents in the collection after deletion:")
docs = students.find({})
for doc in docs:
    print(doc)
