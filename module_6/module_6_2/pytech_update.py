# Gillenwater, Sam
# CYBR410 - Prof Haas

# MongoDB Student Data Management

# This script connects to a MongoDB database and performs operations on a collection named 'students'.
# It retrieves all documents from the collection, updates the last name for a specific student, and displays the updated document.

# Prerequisites!:
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

# Update the last name for student_id 1007
students.update_one({"student_id": 1007}, {"$set": {"last_name": "Gallagher"}})

# Display the updated document
print("\nUpdated document for student_id 1007:")
doc = students.find_one({"student_id": 1007})
print(doc)
