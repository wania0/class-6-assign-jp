"""
Create a dictionary named employee_data with the following key-value pairs:

"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names."""

# Solution :

employee_data = { "John": 55000 , 
    "Emma": 60000 ,
    "Harry": 70000 ,
    "Sophia": 65000 ,
    "Mike": 48000 
}

for key , values in employee_data.items():
    if values > 60000:
        print("Employees who earn more than 60,000:" , key)