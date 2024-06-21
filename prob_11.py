"""
Givent the list of students
students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
]

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. display which class obtained the higher marks
7. display the student name that obtain high marks in subject Math in class 10
8. Add new Student and its subject, score and class in same dict i.e students
"""

# Solution :

students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],#253
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],#243
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],#275
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85], #249
        "Class": 11
    }
]

# 1. display Alice English Score :
print("Alice English Score is:" , students[0]["scores"][2])

# 2. display Bob Class :
print("Bob Class is:" , students[1]["Class"])

# 3. display Charlie Math Score :
print("Charlie Math Score is:" , students [2]["scores"][0])

# 4. display Diana's avg score :
print("Diana's avg score is:" , sum(students[3]["scores"])/len(students[3]["subjects"]))

# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score] :