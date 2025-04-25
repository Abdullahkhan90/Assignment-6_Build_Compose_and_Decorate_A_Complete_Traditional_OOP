## Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:  
    total_books = 0  

    @classmethod  
    def increment_book_count(cls):  
        cls.total_books += 1  

    def __init__(self, title):  
        self.title = title  
        Book.increment_book_count()  

  
b1 = Book("1999")  
b2 = Book("History of OOP")  
b3 = Book("The Lion") 
b4 = Book("The Chocalate Cafe") 

print("Total books:", Book.total_books)  