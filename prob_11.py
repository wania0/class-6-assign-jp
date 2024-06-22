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

student = {"John": 
    {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}
list_len = len(student["John"]["Subjects"])

for i in range(list_len):
    name = "John"
    subject = student["John"]["Subjects"][i]
    score = student["John"]["Scores"][i]
    print("Student:",name ,",", "Subject:" ,subject ,",", "Score:" ,score)
    
# 6. display which class obtained the higher marks :

class_10_score = students[0]["scores"] + students[1]["scores"]
class_11_score = students[2]["scores"] + students[3]["scores"]

total_class_10 = sum(class_10_score)
total_class_11 = sum(class_11_score)

if total_class_10 > total_class_11:
    print("Class 10 obtained the higher marks")
else:
    print("Class 11 obtained the higher marks")

# 7. display the student name that obtain high marks in subject Math in class 10:

alice_math_score = students[0]["scores"][0]
bob_math_score = students[1]["scores"][0]

if alice_math_score > bob_math_score :
    print("The student that obtain high marks in Math in class 10 is : ", students[0]["name"])
else:
    print("The student that obtain high marks in Math in class 10 is : ", students[1]["name"])

# 8. Add new Student and its subject, score and class in same dict i.e students :

another_dict = {
        "name": "Sara",
        "subjects": ["Math", "Science", "English"],
        "scores": [56, 78, 60] ,
        "Class": 12
    }
students.append(another_dict)

for item in students:
    print(item)


    
