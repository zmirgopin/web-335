/**
	Title: gopin-aggregateQueries.js
    Author: Zahava Gopin
    Date: 17 April 2023
    Description: MongoDB Shell queries for houses collection.
 */

//2.	query to show a list of documents in the houses collection
deb.houses.find()
//3.	Write a query to show a list of documents in the student’s collection
db.students.find()
//4.	Write a query to add a document to the student’s collection. write a query to prove the document was added to the user’s collection  
db.students.insertOne({firstName: "Test", lastName: "User", studentId: "s1019", houseId: "h1010"})

db.students.find({firstName:"Test"})
//5.	Write a query to delete the document you created in step 4.write a query to prove the document was deleted to the user’s collection 
db.students.deleteOne({firstName:"Test"})

db.students.find({firstName:"Test"})

//6.	Write a query to show a list of students by house 
db.houses.aggregate([{$lookup:{from: "students", localField: "houseId", foreignField:"houseId", as: "inhabitants"}}])

//Write a query to show a list of students for house Gryffindor 
db.houses.aggregate([{$lookup:{from: "students", pipeline:[{$match: {houseId: "h1007"}}], as: "GryffindorInhabitants"}}]) 