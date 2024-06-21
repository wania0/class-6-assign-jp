"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76

3. Write a for loop to assign grades based on the following criteria:
Score >= 90: Grade A
Score >= 80 and < 90: Grade B
Score >= 70 and < 80: Grade C
Score < 70: Grade D
Store these grades in a new dictionary called student_grades."""

student_scores = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Evan": 76}

student_grades = {}

for key, value in student_scores.items():
    if value >= 90:
        student_grades[key] = "Grade-A"
    elif value >= 80 and value < 90:
        student_grades[key] = "Grade-B"
    elif value >= 70 and value < 80:
        student_grades[key] = "Grade-C"
    else:
        student_grades[key] = "Grade-D"
        
print(student_grades)
        

        