/**
	Title: gopin-mongoDbShell.js
    Author: Zahava Gopin
    Date: 5 April 2023
    Description: MongoDB Shell queries for users collection.
 */

//a query to display all of the documents in the user’s collection
db.users.find()
//Write a query find the user with an email address of jbach@me.com
db.users.find({email: 'jbach@me.com'})
//Write a query to find a user with the last name of Mozart
db.users.find({lastName: 'Mozart'})
//Write a query to find a user with a first name of Richard
db.users.find({firstName: 'Richard'})
//Write a query to find a user with an employeeId of 1010
db.users.find({employeeId: '1010'})