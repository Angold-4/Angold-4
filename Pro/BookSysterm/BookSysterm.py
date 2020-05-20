# Wange 20200518
from PCreditCard import PredatoryCreditCard


class Book:

    def __init__(self, name, author, price, source):
        self._name = name
        self._author = author
        self._price = price
        self._source = source

    def __add__(self, other):
        Answer = 0
        currency = ["$", "$", ":"]
        strnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        cilist = []
        cjlist = []
        ilist = []
        jlist = []
        for i in self._price:
            """i --> self"""
            if i in currency:
                cilist.append(i)
            elif i in strnumber:
                ilist.append(i)

        if type(other) is int or type(other) is float:
            """j --> other"""
            jnumber = other
        else:
            for j in other._price:
                if j in currency:
                    cjlist.append(j)
                elif j in strnumber:
                    jlist.append(j)
            jnumber = float(''.join(jlist))

        inumber = float(''.join(ilist))
        Answer = inumber + jnumber
        if cilist == cjlist:
            return ''.join(cilist)+str(Answer)
        else:
            return Answer

    def __radd__(self, other):
        Answer = 0
        currency = ["$", "$", ":"]
        strnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        cilist = []
        cjlist = []
        ilist = []
        jlist = []
        for i in self._price:
            """i --> self"""
            if i in currency:
                cilist.append(i)
            elif i in strnumber:
                ilist.append(i)

        if type(other) is int or type(other) is float:
            """j --> other"""
            jnumber = other
        else:
            for j in other._price:
                if j in currency:
                    cjlist.append(j)
                elif j in strnumber:
                    jlist.append(j)
            jnumber = float(''.join(jlist))

        inumber = float(''.join(ilist))
        Answer = inumber + jnumber
        if cilist == cjlist:
            return ''.join(cilist)+str(Answer)
        else:
            return Answer


class BookStore:

    def __init__(self):
        self._bookdict = {}
        self._pricedict = {}
        self._sourcedict = {}
        self._book = {}
        self._viplist = []

    def check(self, bookname):
        return self._bookdict.__contains__(bookname)

    def find_price(self, bookname):
        try:
            return self._pricedict[bookname]
        except IndexError as e:
            print("sorry, we don't apply:", bookname, e)

    def find_author(self, bookname):
        try:
            return self._bookdict[bookname]
        except IndexError as e:
            print("sorry, we don't apply:", bookname, e)

    def _append(self, book):
        if isinstance(book, Book):
            if book._name not in self._bookdict:
                _pricedict = {book._name: book._price}
                _authordict = {book._name: book._author}
                _sourcedict = {book._name: book._source}
                self._bookdict.update(_authordict)
                self._pricedict.update(_pricedict)
                self._sourcedict.update(_sourcedict)
                self._book[book._name] = book
            else:
                pass
        else:
            print("Sorry, we only accept books certified by the bookstore")

    def _addcard(self, customer, bank, acnt, limit, apr):
        self._creditcard = PredatoryCreditCard(customer, bank, acnt, limit, apr)

    def _remove(self, bookname):
        if bookname in self._bookdict:
            self._bookdict.pop(bookname)
            self._pricedict.pop(bookname)
            self._sourcedict.pop(bookname)
        else:
            print("name", bookname, "not found")

    def _bevip(self, person):
        if isinstance(person, Person):
            if person in self._viplist:
                print(person._gender, person._name, "You are already our VIP member")
            else:
                if person._creditcard and self._creditcard:
                    person._creditcard.charge(50)
                    self._creditcard.make_payment(50)
                    self._viplist.append(person)
                else:
                    print("Error! Card not found")

    def check_wallet(self):
        if self._creditcard:
            print("Name:", self._creditcard.get_customer())
            print("Bank:", self._creditcard.get_bank())
            print("Account:", self._creditcard.get_account())
            print("Balance:", self._creditcard.get_balance())
            print("Limit:", self._creditcard.get_limit())
        else:
            print("no card yet.you can call '_addcard()' method to add a card")

    def buy(self, person, bookname):
        strnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        ilist = []
        Answer = 0
        if isinstance(person, Person) and bookname in self._bookdict:
            price = self._pricedict[bookname]
            for i in price:
                if i in strnumber:
                    ilist.append(i)
            Answer = float(''.join(ilist))
            if person in self._viplist:
                Answer *= 0.9
        else:
            print("invalid bookname or person")
            return False

        print("You need to Pay: $", Answer)
        print("Processing...")
        person._creditcard.charge(Answer)
        self._creditcard.make_payment(Answer)
        person._bookdict[bookname] = self._sourcedict[bookname]
        print("Finished! :-)")

    def add_shoppinglist(self, person, bookname):
        if bookname in self._bookdict and isinstance(person, Person):
            person._shoppinglist.append(bookname)
        else:
            print("invalid bookname or person")

    def settlement(self, person):
        Total = 0
        if isinstance(person, Person):
            for i in person._shoppinglist:
                Book = self._book[i]
                Total = Total + Book
                person._bookdict[i] = self._sourcedict[i]
            if person in self._viplist:
                Total *= 0.85

            print("You need to Pay: $", Total)
            print("Processing...")
            person._creditcard.charge(Total)
            self._creditcard.make_payment(Total)
            person._shoppinglist = []
            print("Finished! :-)")


class Person:

    def __init__(self, name, gender):
        MS = ['Mr.', 'Miss.']
        self._name = name
        self._bookdict = {}
        self._shoppinglist = []
        try:
            self._gender = MS[gender]
        except IndexError:
            print("gender must be 0(Male) or 1(Female)")

    def _addcard(self, customer, bank, acnt, limit, apr):
        self._creditcard = PredatoryCreditCard(customer, bank, acnt, limit, apr)

    def check_wallet(self):
        if self._creditcard:
            print("Name:", self._creditcard.get_customer())
            print("Bank:", self._creditcard.get_bank())
            print("Account:", self._creditcard.get_account())
            print("Balance:", self._creditcard.get_balance())
            print("Limit:", self._creditcard.get_limit())
        else:
            print("no card yet.you can call '_addcard()' method to add a card")

    def check_order(self):
        return self._bookdict
