"""
 Create a dictionary named student_scores with the following key-value pairs:
 "Alice": 85
 "Bob": 78
 "Charlie": 92
 "Diana": 88
 "Evan": 76

1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score]."""

# SOLUTION :

student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76
}

for name,score in student_scores.items():
    print("Student:", name , ", Score:" , score)






