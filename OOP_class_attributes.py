## Checkin gclass types and instances

#class Book:
#     def __init__(self, title):
#         self.title = title

# class Newspaper:
#     def __init__(self, name):
#         self.name = name
        
# # create some instances
# b1 = Book("The Catcher in the Rye")
# b2 = Book("The Grapes of Wrath")
# n1 = Newspaper('The Washington Post')
# n2= Newspaper('The New York Times')


### use type() to inspect the object type
# print(type(b1))
# print(type(n1))


## compare two types together
# print(type(b1)== type(b2))
# print(type(b1)== type(n2))


### use isinstance to compare a specific instance to a known type

# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(n2, Book))


## PART II
### Using class-level and static method
class Book:
    # TODO : properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO : double-underscore properties are hidden from other classes
    __booklist = None
    # TODO : create a class method 
    @classmethod
    def getbooktypes(cls):
            return cls.BOOK_TYPES
    # TODO : create a static method
    @staticmethod
    def getbooklist():
         if Book.__booklist == None:
              Book.__booklist =[]
         return Book.__booklist

    def setTitle(self, newtitle):
        self.title = newtitle
    
    def __init__(self,title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else: 
            self.booktype = booktype

# TODO : access the class attribute
print("Book types:", Book.getbooktypes())

# TODO : create some book instances
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title2", "PAPERBACK")

# TODO : use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

