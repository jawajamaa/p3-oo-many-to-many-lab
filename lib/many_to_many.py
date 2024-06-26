class Author:
    all = list()

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Name must be of the type string")

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])
    
class Book:
    all = list()

    def __init__(self, title):
            self._title = title
            Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("Title must be of the type string")

    def contracts(self):
        # contract_list = list()
        # for contract in Contract.all:
        #    if contract.book == self:
        #         contract_list.append(contract)
        # return contract_list 
       return [contract for contract in Contract.all if contract.book == self] 
    
    def authors(self):
        return [contract.author for contract in Contract.all]

class Contract:
    all = list()

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date           
        self.royalties = royalties
        type(self).all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of the Author Class")
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book must be an instance of the Book Class")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date must be of the type string")

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):            
            self._royalties = royalties
        else:
            raise Exception("Royalties must be an integer")

# author = Author("Name")
# book = Book("Snow Crash")
# author = Author("Neal Stephenson")
# date = '07/09/1992'
# royalties = 40000
# contract = Contract(author, book, date, royalties)

# print(contract)
# print(Author.books(book))
