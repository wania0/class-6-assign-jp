"""
Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. Add new Student and its subject, score and class in same dict i.e students
7. add new subject and its score in John
"""

# Solution :

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

# 1. display Alice English Score:
print("Alice English score is:" , students ["Alice"]["Scores"][2])

# 2. display Bob Class:
print("Bob class is:" , students ["Bob"]["Class"])

# 3. display Charlie Math Score:
print("Charlie math score is:" , students ["Charlie"]["Scores"][0] )

# 4. display Diana's avg score:

diana_data = students["Diana"]
diana_score = diana_data["Scores"]
sum = 0
for items in  diana_score:
    sum = sum + items
    avg = sum / 3
print("Diana's avg score is:" , avg)

# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score]:

list_len = len(students["John"]["Subjects"])
for i in range(list_len):
    name = "John"
    subject = students["John"]["Subjects"][i]
    score = students["John"]["Scores"][i]
    print("Student:",name ,",", "Subject:" ,subject ,",", "Score:" ,score)

# 6. Add new Student and its subject, score and class in same dict i.e students:

another_dict = {"Zara":{"Subjects" :["Maths" , "Science" , "English"] , "Scores" : [60 , 78 , 54] , "Class" : 10}}
students.update(another_dict)

for key , values in students.items():
    print(key,values)

# 7. add new subject and its score in John :

john_data = students["John"]

new_subject = "History"
new_score = 70

john_data["Subjects"].append(new_subject)
john_data["Scores"].append(new_score)

for key , values in john_data.items():
    print(key , values)
