from flask import render_template, request, redirect
from app import app
from models.book import *
from models.books import *

@app.route('/books')
def list_books():
    return render_template('index.html', title='Home', books = books)


@app.route('/books', methods = ["POST"])
def add_books():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_in = True if "checked_in" in request.form else False
    checked_out = True if "checked_out" in request.form else False
    new_book = Book(title = title, author = author, genre = genre, checked_in = checked_in, checked_out = checked_out)
    add_book_to_list(new_book)
    return redirect("/books")

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
    delete_book(int(index))
    return redirect('/books')

@app.route('/books/<index>')
def book(index):
    book = books[int(index)]
    return render_template('book.html', title="single book",book = book)


    
