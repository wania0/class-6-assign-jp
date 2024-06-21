""" Create a dictionary named employee_data with the following key-value pairs:

"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly."""

# Solution :

employee_data = { "John": 55000 , 
    "Emma": 60000 ,
    "Harry": 70000 ,
    "Sophia": 65000 ,
    "Mike": 48000 
}

for key , values in employee_data.items():
    salary = values * 0.1 
    new_salary =  values + salary 
    employee_data[key] = new_salary

print( "The salary of each employee increased by 10% :\n", employee_data)