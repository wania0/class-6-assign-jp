"""

Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2

1. Write a for loop to add 2 more copies to each book. Update the dictionary accordingly.

"""

# Solution :

library_books = {
    "The Great Gatsby": 4 ,
    "1984": 6 ,
    "To Kill a Mockingbird": 3 ,
    "The Catcher in the Rye": 5 ,
    "Moby Dick": 2
}

for key , values in library_books.items():
    updated_copies = values + 2
    library_books[key] = updated_copies
    
print(library_books)
    


