#	Title: gopin_usersp1.py
#   Author: Zahava Gopin
#   Date: 24 April 2023
#   Description: Connecting python queries to MongoDB collection. 
from pymongo import MongoClient

client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.r06aetm.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)
# Access the desired database and collection
db= client.web335DB
collection= db.users
# Find all documents in the collection
documents = collection.find()
print(documents)
# Find the document with the specified id
employee= collection.find_one({'employeeId': '1011'})
# Print the document
print(employee)
# Find the document with the specified name
name= collection.find_one({'lastName': 'Mozart'})
# Print the document
print(name)