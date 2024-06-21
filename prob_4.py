"""

Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76

4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.

"""

# SOLUTION :

student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76
}

updated_student_scores = {}

for key , values in student_scores.items():
    bonus = values + 5
    updated_student_scores[key] = bonus
    
print("Updated dictionary is given below:")
print(updated_student_scores)

