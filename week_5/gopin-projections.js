/**
	Title: gopin-projections.js
    Author: Zahava Gopin
    Date: 10 April 2023
    Description: MongoDB Shell queries for users collection.
 */

//Write a query to add a new user to the user’s collection
db.users.insertOne({ firstName: 'John', lastName: 'Doe', employeeId: '1234', email: 'john@doe.com', dateCreated: new Date});
//Write a query to update Mozart’s email address to mozart@me.com.
db.users.update({email:"wmozart@me.com"}, {$set : {email:"mozart@me.com"}})
//Next, write a query to prove the email address was updated
db.users.find({email: 'mozart@me.com'})
//Write a query to list all documents in the user’s collection.  Use projections to only display the firstName, lastName, and email fields
db.users.find({}, {firstName:1, lastName: 1, email:1, _id: 0})