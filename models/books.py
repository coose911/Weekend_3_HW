from models.book import *

book_1 = Book( "Harry Potter and the goblet of fire", "JK.Rowling", "Adventure", True, False)
book_2 = Book("Harry Potter and the chamber of secrets", "JK.Rowling", "Adventure", True, False)
book_3 = Book("Didley Squat", "Jeremy Clarkson", "Humour", False, True)

books = [book_1, book_2, book_3]

def add_book_to_list(book):
    books.append(book)

def delete_book(book):
    books.pop(book)

