class Book:
    def __init__(self,author,title):
        self.title=title
        self.author=author
        self.is_borrow=False
    def borrow(self):
        if self.is_borrow==False:
            self.is_borrow=True
            print(f"{self.title} is borrowed")
        else:
            print("No")
    def return_book(self):
        if self.is_borrow:
            self.is_borrow=False
            print(f"{self.title} was returned")
        else:
            print(f"{self.title} was not borrowed")
    def __str__(self):
        status="Available" if not self.is_borrow else "Borrowed"
        return f"{self.title} by {self.author} - {status}"
class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,title,author):
        book=Book(author,title)
        self.book.append(book)
        print(f"{title} by {author} added to the library")
    def remove_book(self,title):
        for book in self.book:
            if book.title==title and not book.is_borrow:
                self.book.remove(book)
                print("Book is removed fro the library")
            else:
                print("Book is either borrowed or doesnt exist")
    def show_books(self):
        if not self.book:
            print("Book is not in the library")
        else:
            for book in self.book:
                print(book)
    def borrow_book(self,title):
        for book in self.book:
            if book.title==title:
                book.borrow()
                return
            print("Book is not availabe in the library")
    def return_book(self,title):
        for book in self.book:
            if self.title==title:
                book.remove_book()
                return
            print("Book was not borrowed")
library=Library()
library.add_book("Enigmtix","Tauqeer")
library.show_books()
library.borrow_book("Enigmatix")
library.remove_book("Enigmatix")
library.show_books()