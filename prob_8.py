"""

Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2

2. Write a for loop to calculate the total number of books in the library. Print the total count.

"""

# Solution :

library_books = {
    "The Great Gatsby": 4 ,
    "1984": 6 ,
    "To Kill a Mockingbird": 3 ,
    "The Catcher in the Rye": 5 ,
    "Moby Dick": 2
}

book_count = 0

for values in library_books.values():
    book_count += values
    
print("The total number of books in the library are :" , book_count , "books")
    

