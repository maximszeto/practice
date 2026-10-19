import os
import time

os.system("clear")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        #self.is_checked_out = False  # Books start out available!
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
        found = False
 

        for each_book in self.books:
            if each_book.title == book_object.title:
                each_book.quantity += 1
                found = True
                break

        if found == False: 
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
            if each_book.title == book_obj.title and each_book.quantity > 0:
                if len(patron_obj.borrowed_books) >= 10:
                    print("Sorry but you have checked out your maximum amount of books")
                    return
                patron_obj.reading_history.append(book_obj)
                patron_obj.borrowed_books.append(book_obj)
                print(f"\n{patron_obj.name} successfully checked out {book_obj.title}")
                each_book.quantity -= 1
                return
        
            elif each_book.title == book_obj.title and each_book.quantity <= 0:
                print(f"\nSorry but all the copies of {each_book.title} are checked out")
                return

        print(f"Sorry but we do not seem to have that book in our library")   
                
        
        

    def return_book(self, book_obj , patron_obj):
        for each_book in self.books:
            if each_book.title == book_obj.title and book_obj in patron_obj.borrowed_books: 
                patron_obj.borrowed_books.remove(book_obj)
                print(f"{patron_obj.name} returned the book {each_book.title}")
                each_book.quantity += 1
                return

            elif each_book.title == book_obj.title and book_obj not in patron_obj.borrowed_books:
                print(f"{patron_obj.name} doesn't have {each_book.title} even checked out")
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


# ==========================================
# TEST SCRIPT FOR CRITICAL LOGIC & BUG FIXES
# ==========================================

"""
# 1. Setup the Library
lib = Library("Test Library")

# 2. Create books (Notice we are adding TWO copies of "The Hobbit")
hobbit_copy1 = Book("The Hobbit", "J.R.R. Tolkien")
hobbit_copy2 = Book("The Hobbit", "J.R.R. Tolkien")
dune = Book("Dune", "Frank Herbert")

lib.add_book(hobbit_copy1)
lib.add_book(hobbit_copy2) # Total quantity of "The Hobbit" should now be 2
lib.add_book(dune)

# 3. Create Patrons
alice = Patron("Alice")
bob = Patron("Bob")

print("--- STARTING TESTS ---")

# TEST 1: Multiple copies availability
print("\n[Test 1] Alice checks out Copy 1 of The Hobbit...")
lib.check_out(hobbit_copy1, alice) 
# EXPECTED: Alice successfully checks it out. Remaining quantity of "The Hobbit" is 1.

print("\n[Test 2] Bob tries to check out Copy 2 of The Hobbit...")
lib.check_out(hobbit_copy2, bob)
# EXPECTED: Bob should successfully check it out because quantity was 1! 
# (If your code still relies on a single 'is_checked_out' boolean, this will fail or say it's already out).

print("\n[Test 3] Alice tries to check out Dune (which is available)...")
lib.check_out(dune, alice)
# EXPECTED: Alice successfully checks out Dune.

print("\n[Test 4] Bob tries to return a copy of The Hobbit...")
lib.return_book(hobbit_copy2, bob)
# EXPECTED: Bob successfully returns it. Quantity of "The Hobbit" goes back to 1.
# Alice should STILL have her copy checked out.

print("\n--- FINAL STATUS CHECK ---")
lib.show_books() 
# EXPECTED: 
# "The Hobbit has 1 copies available"
# "Dune has 0 copies available"

alice.display_books()
# EXPECTED: Should show "The Hobbit" and "Dune"

bob.display_books()
# EXPECTED: Should be empty (or show nothing) because he returned his book.
"""


def main():

    library_name = input("Welcome! What will this library be called?: ")
    lib = Library(library_name)

    patron_name = input("What is your name patron?: ")
    patron_user = Patron(patron_name)

    user_prompt = "" 

    while user_prompt != "9":
        os.system("clear")
        user_prompt = input(f"""Welcome to the {library_name} Library, {patron_name}!
You are currently using {patron_name}'s account

        Here is everything you can do:\n
        1. Add a book to the {library_name} library
        2. Checkout a book
        3. Return a book 
        4. Show all the books in the {library_name} Library
        5. Show all the patrons of the {library_name} Library
        6. Show the books you have checked out currently
        7. Show all the books you have checked out
        8. Change User
        9. Exit
        Please use the number to do what you wanna do:  """)

        if user_prompt == "1":
            os.system("clear")
            user_book_title = input("What is the title of the book that you would like to add to the library?: ")
            user_book_author = input(f"What is the author of {user_book_title}")
            book = Book(user_book_title, user_book_author)
            lib.add_book(book)
            print(f"Successfully added {user_book_title} to the {library_name} Library")
            lib.show_books()
            time.sleep(5)

        elif user_prompt == "2":
            os.system("clear")
            pass

        elif user_prompt == "3":
            os.system("clear")
            pass

        elif user_prompt == "4":
            os.system("clear")
            pass


        elif user_prompt == "5":
            os.system("clear")
            pass

        elif user_prompt == "6":
            os.system("clear")
            pass


        elif user_prompt == "7":
            os.system("clear")
            pass

main()
