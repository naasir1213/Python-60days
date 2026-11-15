"""Python is a case-sensitive programming language.
This means that it treats uppercase and lowercase characters differently.
 For example, the variable name "Variable" is different from "variable"."""
#By using snake_case is the best for variable defined.
employee_name = "Naasir"
experience = 12
salary = 10000
is_automation_tester = True

print("Employee Name:",employee_name)
print("Experience:",experience)
print("Salary:",salary)
print("Automation Tester:",is_automation_tester)

print(type(employee_name))
print(type(experience))
print(type(salary))
print(type(is_automation_tester))

#QA Automation real-time example
#Suppose we need to validate a login API response

response={
"username":"admin",
"status_code":200,
"is_authenticated":True,
"response_Time":1.25
}
print(type(response["username"]))
print(type(response["status_code"]))
#We need to validate the API response schemas and identifying the data type mismatches.

#Task
"""
Create four variables:
1. employee_name – Store a name.
2. employee_age – Store an age.
3. employee_salary – Store a salary with decimal values.
4. is_permanent – Store True or False.
Then:
- Print all four values.
- Print the data type of each variable using type().
"""
employee_name="Mohammad"
employee_age=36
employee_salary=10003
is_permanent=True

print("Employee name is:", employee_name)
print("Employee age is:", employee_age)
print("Employee salary is:", employee_salary)
print("Is Permanent:", is_permanent)
print(type(employee_name))
print(type(employee_age))
print(type(employee_salary))
print(type(is_permanent))

#TypeCasting
#API returns employee age as a string.
api_age="36"
expected_age=36
print(type(api_age))
print(type(expected_age))
#compare both variables using ==
print(api_age==expected_age)

#Real time automation scenario
#How to handle a string-to-integer conversion before validating API data.
"""
respone={
    "employee_age":"36"
}
expected_age=36

actual_age= int(response["employee_age"])
assert 
actual_age==expected_age
"""