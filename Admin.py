from Books import Book
from Users import User
from Library import Library


class Admin:
    def __init__(self):
        self.library = Library()

    def menu(self):
        while True:
            print("\n       LIBRARY MANAGEMENT SYSTEM     ")
            print("1. Add Book")
            print("2. Show All Books")
            print("3. Add User")
            print("4. Show All Users")
            print("5. Borrow Book")
            print("6. Return Book")
            print("7. View User Borrow History")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()

            elif choice == '2':
                self.library.show_books()

            elif choice == '3':
                self.add_user()

            elif choice == '4':
                self.library.show_users()

            elif choice == '5':
                self.borrow_book()

            elif choice == '6':
                self.return_book()

            elif choice == '7':
                self.view_user_history()

            elif choice == '8':
                print("Exiting system. Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

    def add_book(self):
        try:
            book_id = int(input("Enter Book ID: "))
            name = input("Enter Book Name: ")
            book = Book(book_id, name)
            self.library.add_book(book)
        except ValueError:
            print("Invalid input.")

    def add_user(self):
        try:
            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")
            user = User(user_id, name)
            self.library.add_user(user)
        except ValueError:
            print("Invalid input.")

    def borrow_book(self):
        try:
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))

            user = None
            book = None
            for u in self.library.users:
                if u.id == user_id:
                    user = u
                    break

            for b in self.library.books:
                if b.id == book_id:
                    book = b
                    break

            if user and book:
                user.borrow_book(book)
            else:
                print("Invalid User ID or Book ID.")
        except ValueError:
            print("Invalid input.")

    def return_book(self):
        try:
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))

            user = None
            book = None
            for u in self.library.users:
                if u.id == user_id:
                    user = u
                    break

            for b in self.library.books:
                if b.id == book_id:
                    book = b
                    break

            if user and book:
                user.return_book(book)
            else:
                print("Invalid User ID or Book ID.")
        except ValueError:
            print("Invalid input.")

    def view_user_history(self):
        try:
            user_id = int(input("Enter User ID: "))
            
            user = None
            for u in self.library.users:
                if u.id == user_id:
                    user = u
                    break

            if user:
                user.view_history()
            else:
                print("User not found.")
        except ValueError:
            print("Invalid input.")

admin = Admin()
admin.menu()