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
        print(f"\nBooks in the {self.name} Library")
        for book in self.books:
            print(f"{book} by {book.author} has {book.quantity} copies avaliable")

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

    def change_patron_account(self, patron, library):
        if len(library.patrons) <= 1:
            print("You can not switch into another person's account right now")
            time.sleep(2.5)
            return None
        else: 
            for each_patron in library.patrons:
                if each_patron.name == patron:
                    return each_patron


def main():

    library_name = input("Welcome! What will this library be called?: ")
    lib = Library(library_name)

    patron_name = input("What is your name patron?: ")
    patron_user = Patron(patron_name)
    lib.patrons.append(patron_user)


    user_prompt = "" 

    while user_prompt != "9":
        os.system("clear")
        user_prompt = input(f"""Welcome to the {library_name} Library, {patron_user.name}!
You are currently using {patron_user.name}'s account

        Here is everything you can do:\n
        1. Add a book to the {library_name} library
        2. Checkout a book
        3. Return a book 
        4. Show all the books in the {library_name} Library
        5. Show all the patrons of the {library_name} Library
        6. Show the books you have checked out currently
        7. Add User
        8. Change patron account
        9. Exit
        Please use the number to do what you wanna do:  """)

        if user_prompt == "1":
            os.system("clear")
            user_book_title = input("What is the title of the book that you would like to add to the library?: ")
            user_book_author = input(f"What is the author of {user_book_title}: ")
            book = Book(user_book_title, user_book_author)
            lib.add_book(book)
            lib.show_books()
            time.sleep(2.5)

        elif user_prompt == "2":
            os.system("clear")
            print("Avaliable books")
            lib.show_books()
            user_title_check_out = input("\nWhat is the title of the book would you like to check out?: ")
            user_author_check_out = input(f"\nWhat is the author of {user_title_check_out}?: ")
            book_checked_out = Book(user_title_check_out, user_author_check_out)
            lib.check_out(book_checked_out, patron_user)
            patron_user.display_books()
            time.sleep(2.5)

        elif user_prompt == "3":
            os.system("clear")
            print(f"Here are the books that {patron_name} has checked out")
            patron_user.display_books()
            user_return_title = input("\nWhat is the name of the book would you like to return:? ")
            for the_books in patron_user.borrowed_books:
                if user_return_title == the_books.title:
                    lib.return_book(the_books, patron_user)
                    break
            time.sleep(2.5)
            os.system("clear")
            pass

        elif user_prompt == "4":
            os.system("clear")
            if lib.books == []:
                print(f"There are no books in the {library_name} library at this moment")
            else:
                lib.show_books()
            time.sleep(2.5)
            os.system("clear")
            pass

            
            # show all patrons in the library
        elif user_prompt == "5":
            os.system("clear")
            if lib.patrons == []:
                print("there are no patrons in this library")
            else:
                lib.show_patrons()
            time.sleep(2.5)
            os.system("clear")
            pass

        # 6. Show the books you have checked out currently
        elif user_prompt == "6":
            os.system("clear")
            print(f"here are all the books {patron_user.name} has checked out")
            for book in patron_user.borrowed_books:
                print(f"- {book}")
                time.sleep(2.5) 
            


        # 7. Add User
        elif user_prompt == "7":
            os.system("clear")
            new_patron = input("What should this new users name be?: ")
            patron = Patron(new_patron)
            lib.patrons.append(patron)
            lib.show_patrons()
            time.sleep(2.5)
            pass

        # 8. Change User
        elif user_prompt == "8":
            os.system("clear")
            lib.show_patrons()
            print(f"You are currently using {patron_user.name}'s account\n")
            patron_switch = input("Which patron account would you like to switch to?: ")
            selected_patron = patron_user.change_patron_account(patron_switch, lib)
            if selected_patron == None:
                print("We could not find the user you were trying to switch to")
                time.sleep(2.5)
            else:
                patron_user = selected_patron
                print(f"You successfully changed to {patron_user.name}'s account")

os.system("clear")

main()
