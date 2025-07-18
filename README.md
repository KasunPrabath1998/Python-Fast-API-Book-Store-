
// Add book
http://127.0.0.1:8000/books

{
  "title": "Harry Potter",
  "author": "J.K. Rowling",
  "price": 200
}


// Get books
http://127.0.0.1:8000/books 


// Get book by ID
http://127.0.0.1:8000/books/2


// Update book by ID
http://127.0.0.1:8000/books/2
{
  "title": "Harry Potter and the Chamber of Secrets",
  "author": "J.K. Rowling",
  "price": 225 
}


// Delete book by ID
http://127.0.0.1:8000/books/8


// Search books by title
GET http://127.0.0.1:8000/books/search/?title=harry

