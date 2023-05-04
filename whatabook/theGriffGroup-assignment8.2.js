/**
	Title: theGriffGroup-assignment8.2.js
    Author: Megan Walker, Brooks, Zahava Gopin
    Date: 4 May 2023
    Description: Queries for the whatabook application
 */

// Write a query to display a list of books.

db.books.find({})

// Write a query to display a list of books by genre.

db.books.find({ genre: "Science Fiction" })

// Write a query to display a list of book by author.

db.books.find({ author: "J. R. R. Tolkien" })

// Write a query to display a book by bookId.

db.books.findOne({ bookId: 5 })