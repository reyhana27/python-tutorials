class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    
    def borrowBook(self):
        if self.available == True:
            print("book successfully borrowed")
            self.available = False
        elif self.available == False:
            print("The book is not avaiable at the moment")
    
    def returnBook(self):
        if self.available == False:
            self.available = True
        print("thanks for returning")

    def displayInfo(self):
        print(f"Title: {self.title}, Author: {self.author}, available: {self.available}")
    
book1 = Book("Cookbook", "rosy", True)
book2 = Book("Apples", "george", True)
book3 = Book("glisten", "emily", True)
book4 = Book("dino", "earl", True)
book5 = Book("teas", "bob", True)

bookList = [book1, book2, book3, book4, book5]

book2.borrowBook()
book3.borrowBook()
book4.borrowBook()
for Book in bookList:
    Book.displayInfo()
