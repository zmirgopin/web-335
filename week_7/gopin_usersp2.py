#	Title: gopin_usersp2.py
#   Author: Zahava Gopin
#   Date: 26 April 2023
#   Description: Connecting python queries to MongoDB collection. 


from pymongo import MongoClient
import datetime
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.r06aetm.mongodb.net/web335DBretryWrites=true&w=majority")

db= client['web335DB']
#	Write the Python code to create a new user document
jane = {
    'firstName': 'Jane',
    'lastName': 'Doe',
    'employeeId': '1020',
    'email': 'JDoe@me.com',
    'dateCreated': datetime.datetime.now()
}
#insert user document into collection
jane_user_id = db.users.insert_one(jane).inserted_id
print(jane_user_id)

#	Write the Python code to display the newly created document 
print(db.users.find_one({"employeeId": "1020"}))

#	Write the Python code to update the email address of the document   you created in step 2.
db.users.update_one(
    {"employeeId": "1020"},
    {
        "$set": {
            "email": "Jane@me.com"
        }
    }
)

#	Write the Python code to display the updated document.
print(db.users.find_one({"employeeId": "1020"}))

#	Write the Python code to delete the document you created in step 3.
delete = db.users.delete_one({
    "employeeId": "1020"
})

#	Write the Python code to prove the document was deleted
print(db.users.find_one({"employeeId": "1020"}))