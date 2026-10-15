import os

os.system("clear")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False  # Books start out available!
        self.quantity = 0
    
    def __str__(self):
        return f"{self.title}"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] 
        self.patrons = []
    
    def show_books(self):
        print(f"\nBooks in the {self.name}")
        for book in self.books:
            print(f"{book} has {book.quantity} copies avaliable")

    def show_patrons(self):
        print("\nPatrons:")
        for patron in self.patrons:
            print(f"- {patron.name}")

    def add_book(self, book_object):
        # TODO: Append the book_object to the self.books list
        self.books.append(book_object)
        book_object.quantity += 1 

    def check_out(self, book_obj, patron_obj):
        # TODO: Look through self.books. If a book matches the title 
        # and isn't checked out, change its is_checked_out to True.
        if patron_obj not in self.patrons:
            self.patrons.append(patron_obj)
        else:
            pass

        for each_book in self.books:
            if each_book.title == book_obj.title and each_book.is_checked_out == False and each_book.quantity > 0:
                if len(patron_obj.borrowed_books) >= 10:
                    print("Sorry but you have checked out your maximum amount of books")
                    return
                patron_obj.reading_history.append(book_obj)
                patron_obj.borrowed_books.append(book_obj)
                each_book.is_checked_out = True
                print(f"\n{patron_obj.name} successfully checked out {book_obj.title}")
                each_book.quantity -= 1
                return
        
            elif each_book.title == book_obj.title and each_book.is_checked_out == True:
                print(f"\nSorry but {each_book.title} is already checked out")
                return

        print(f"Sorry but we do not seem to have that book in our library")   
                
        
        

    def return_book(self, book_obj , patron_obj):
        for each_book in self.books:
            if each_book.title == book_obj.title and each_book.is_checked_out == True:
                each_book.is_checked_out = False
                patron_obj.borrowed_books.remove(book_obj)
                print(f"{patron_obj.name} returned the book {each_book.title}")
                each_book.quantity += 1
                return

            elif each_book.title == book_obj.title and each_book.is_checked_out == False:
                print(f"{patron_obj.name} dont have {each_book.title} even checked out")
                return

    def sort_books(self, author):
        print(f"Books with the Author {author}:") 
        for book in self.books:
            if book.author == author:
                print(f"{book}") 


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.reading_history = []

    def display_books(self):
        print(f"\nHere are the books that {self.name} has checked out")
        for book in self.borrowed_books:
            print(f"- {book}")

    def display_reading_history(self):
        print(f"\nHere are all your books that {self.name} has read at our library:")
        for book in self.reading_history:
            print(f"- {book}")


book1 = Book("Way of Kings", "Brandon Sanderson")
book2 = Book("Words of Radiance", "Brandon Sanderson")
book3 = Book("Oathbringer", "Brandon Sanderson")
book4 = Book("Rythmn of War", "Brandon Sanderson")
book5 = Book("Wind and Truth", "Brandon Sanderson")


maxim = Patron("Maxim")
ben = Patron("Ben")

lib = Library("Tokyo Library")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)
lib.add_book(book5)

lib.show_books()

lib.check_out(book2, ben)

lib.check_out(book1, maxim)
lib.check_out(book2, maxim)
lib.check_out(book3, maxim)
lib.check_out(book4, maxim)
lib.check_out(book5, maxim)
lib.return_book(book3, maxim)

lib.show_books()

maxim.display_books()
maxim.display_reading_history()
lib.show_patrons()