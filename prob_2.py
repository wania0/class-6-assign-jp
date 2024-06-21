"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76

2. Write a for loop to calculate the average score of the students. Print the average score."""

# SOLUTION :

student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76
}

total_score = 0

for score in student_scores.values():
    total_score += (score)/5

print("The average score of the students:" , total_score)