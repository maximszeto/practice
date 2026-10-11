import os

os.system("clear")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False  # Books start out available!
    
    def __str__(self):
        return f"{self.title}"
    
class Library:
    def __init__(self):
        # This will hold a collection of Book objects
        self.books = [] 
    
    def show_books(self):
        for book in self.books:
            print(book)

    def add_book(self, book_object):
        # TODO: Append the book_object to the self.books list
        self.books.append(book_object)
        

    def check_out(self, book_title):
        # TODO: Look through self.books. If a book matches the title 
        # and isn't checked out, change its is_checked_out to True.
        for book in self.books:
            if book.title == book_title and book.is_checked_out == False:
                book.is_checked_out = True
                print(f"You successfully checked out {book.title}")
                return
        
            elif book.title == book_title and book.is_checked_out == True:
                print(f"Sorry but {book.title} is already checked out")
                return

        print(f"Sorry but we do not seem to have that book in our library")   
                
        
        

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title and book.is_checked_out == True:
                book.is_checked_out = False
                print(f"You returned the book {book.title}")


    def sort_books(self, author):
        print(f"Books with the Author {author}:") 
        for book in self.books:
            if book.author == author:
                print(f"{book}") 

book1 = Book("Words of Radiance", "Brandon Sanderson")
book2 = Book("Oathbringer", "Brandon Sanderson")


lib = Library()

lib.add_book(book1)
lib.add_book(book2)

lib.show_books()

lib.check_out(book2.title)
lib.check_out(book2.title)