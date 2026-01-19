from Users import User


class Book:
    def __init__(self, id, name, available=True):
        self.id = id
        self.name = name
        self.available = available
        self.assigned_user = None

    def display_book(self):
        if self.available == True:
            status = "Available"
        else:
            status = "Not Available"
        if self.assigned_user:
            print(f"ID: {self.id}, Name: {self.name}, Status: {status}, Borrowed by: User Name {self.assigned_user.name}")
        else:
            print(f"ID: {self.id}, Name: {self.name}, Status: {status}")
    
    def check_availability(self):
        return self.available
    
    def borrow_book(self, user):
        if self.check_availability():
            self.available = False
            self.assigned_user = user
            print(f"'{self.name}' has been borrowed.")
        else:
            print(f"'{self.name}' is not available.")

    def return_book(self):
        self.available = True
        self.assigned_user = None
        print(f"'{self.name}' has been returned.")