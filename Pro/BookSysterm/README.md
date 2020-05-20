## BookSysterm

**A BookStore Management System**

```python

def Test():
    A = Book('A', 'a', '$:89', 'amazon')
    B = Book('B', 'b', '$:68.9', 'amazon')
    print(A + B)  # $:157.9
    print(78.9 + A)  # 167.9

    B1 = Book('When Breath Becomes Air', 'Paul Kalanithi', '$:12.16', 'https://www.amazon.com/When-Breath-Becomes-Paul-Kalanithi/dp/081298840X')
    B2 = Book('This is Water', 'David Foster Wallace', '$:9.99', 'https://www.amazon.com/This-Water-Delivered-Significant-Compassionate/dp/0316068225')
    B3 = Book('Meditations', 'Marcus Aureliusk', '$:2.99', 'https://www.amazon.com/Meditations-Marcus-Aurelius/dp/1503280462')
    B4 = Book('A Brief History of Time', 'Stephen Hawking', '$:12.96', 'https://www.amazon.com/Brief-History-Time-Stephen-Hawking/dp/0553380168')
    B5 = Book('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', '$:12.86', 'https://www.amazon.com/Sapiens-Humankind-Yuval-Noah-Harari/dp/0062316095')

    bookstore = BookStore()
    bookstore._append(B1)
    bookstore._append(B2)
    bookstore._append(B3)
    bookstore._append(B4)
    bookstore._append(B5)
    bookstore._addcard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 0.0825)

    Peter = Person('Peter', 0)
    Peter._addcard('Peter Wong', 'California Savings', '5391 0375 9387 6789', 10000, 0.0725)
    Ray = Person('Ray', 1)
    Ray._addcard('Raybb', 'California Savings', '5391 0375 9387 0131', 9000, 0.0736)
    bookstore._bevip(Ray)
    bookstore._bevip(Ray)

    bookstore.buy(Peter, 'Meditations')
    Peter.check_wallet()
    print(Peter.check_order())
    bookstore.check_wallet()
    print('')

    bookstore.add_shoppinglist(Peter, 'This is Water')
    bookstore.add_shoppinglist(Peter, 'When Breath Becomes Air')
    bookstore.add_shoppinglist(Peter, 'A Brief History of Time')
    bookstore.settlement(Peter)
    Peter.check_wallet()
    bookstore.check_wallet()
    print('')

    bookstore.add_shoppinglist(Ray, 'This is Water')
    bookstore.add_shoppinglist(Ray, 'When Breath Becomes Air')
    bookstore.add_shoppinglist(Ray, 'A Brief History of Time')
    bookstore.add_shoppinglist(Ray, 'Meditations')
    bookstore.settlement(Ray)
    Ray.check_wallet()
    bookstore.check_wallet()

```

```
➜  BookSysterm (master) ✗ python3 Test.py

$:157.9
167.9
Miss. Ray You are already our VIP member
You need to Pay: $ 2.99
Processing...
Finished! :-)
Name: Peter Wong
Bank: California Savings
Account: 5391 0375 9387 6789
Balance: 2.99
Limit: 10000
{'Meditations': 'https://www.amazon.com/Meditations-Marcus-Aurelius/dp/1503280462'}
Name: John Bowman
Bank: California Savings
Account: 5391 0375 9387 5309
Balance: -52.99
Limit: 2500

You need to Pay: $ 35.11
Processing...
Finished! :-)
Name: Peter Wong
Bank: California Savings
Account: 5391 0375 9387 6789
Balance: 38.1
Limit: 10000
Name: John Bowman
Bank: California Savings
Account: 5391 0375 9387 5309
Balance: -88.1
Limit: 2500

You need to Pay: $ 32.385
Processing...
Finished! :-)
Name: Raybb
Bank: California Savings
Account: 5391 0375 9387 0131
Balance: 82.38499999999999
Limit: 9000
Name: John Bowman
Bank: California Savings
Account: 5391 0375 9387 5309
Balance: -120.48499999999999
Limit: 2500

```
