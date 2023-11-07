class Book:
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price
    
    def View(self):
        print(f'The title of the book is: {self.Title}')
        print(f'The author of the book is: {self.Author}')
        print(f'The price of the book is: {self.Price}')

myBook = Book("Nostromo", "Joseph Conrad", "£8.99")
myBook.View()