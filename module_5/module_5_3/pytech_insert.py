from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client.pytech
students = db.students

# Create the new student documents
student1 = {"student_id": 1007, "first_name": "Shaquille", "last_name": "Oneal"}

student2 = {"student_id": 1008, "first_name": "Kobe", "last_name": "Bryant"}

student3 = {"student_id": 1009, "first_name": "Michael", "last_name": "Jordan"}

# Insert the new student documents and get the inserted IDs
student1_id = students.insert_one(student1).inserted_id
student2_id = students.insert_one(student2).inserted_id
student3_id = students.insert_one(student3).inserted_id

# Display the inserted IDs
print("Inserted student IDs:")
print(student1_id)
print(student2_id)
print(student3_id)