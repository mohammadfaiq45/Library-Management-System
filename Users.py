class User:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.user_borrowed_books = []
        self.user_borrowed_history = []

    def borrow_book(self, book):
        if book.check_availability():
            book.borrow_book(self)
            book_obj = {
                'book_id': book.id,
                'book_name': book.name
            }
            self.user_borrowed_books.append(book_obj)
            self.user_borrowed_history.append(book_obj)
        else:
            print("Book is not available.")

    def return_book(self, book):
        for b in self.user_borrowed_books:
            if b['book_id'] == book.id:
                self.user_borrowed_books.remove(b)
                book.return_book()
                return
        print("This book was not borrowed by the user.")


    def view_history(self):
        if not self.user_borrowed_history:
            print(f"{self.name} has not borrowed any books yet.")
        else:
            print(f"\n{self.name}'s Borrow History:")
            for book_name in self.user_borrowed_history:
                print(book_name) 