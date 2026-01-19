class Library:
    def __init__(self):
        self.books = []   
        self.users = []   

    def add_book(self, book):
        for b in self.books:
            if b.id == book.id:
                print("Book with this ID already exists.")
                return
        self.books.append(book)
        print(f"Book '{book.name}' added to library.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
            return

        print("\nLibrary Books:")
        for book in self.books:
            book.display_book()

    def add_user(self, user):
        for u in self.users:
            if u.id == user.id:
                print("User with this ID already exists.")
                return
        self.users.append(user)
        print(f"User '{user.name}' added to library.")

    def show_users(self):
        if not self.users:
            print("No users registered.")
            return

        print("\nLibrary Users:")
        for user in self.users:
            print(f"ID: {user.id}, Name: {user.name}")