employee_name="Naasir"
experience=5
salary=50000.50
is_active=True

print(type(employee_name))
print(type(experience))
print(type(salary))
print(type(is_active))

#Important examples
a="100"
a=int(100)
result=a+50
print(result)
print(type(result))

#Another example
print(bool(""))
print(bool("Naasir"))
print(bool(0))
print(bool(1))

#Type Error
#a=10
#b="20"
#result=a+b

#Value Error
#age="Naasir"
#print(int(age)) #Value Error

"""
Write a Python program that stores the following employee information in variables:
- Employee name: Naasir
- Experience: 12
- Salary: 45000.50
- Is active: True
Requirements:
1. Store each value in a separate variable.
2. Print all four values.
3. Display the data type of each variable using type().
4. Print the employee details in a readable format.
Expected output format:
Employee Name: Naasir
Experience: 12
Salary: 45000.5
Is Active: True

Data Types:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

"""
employee_name="Naasir"
experience=12
salary=45000.50
is_active=True

print(f"Employee Name:{employee_name}")
print(f"Experience:{experience}")
print(f"Salary:{salary}")
print(f"Is Active:{is_active}")

print(type(employee_name))
print(type(experience))
print(type(salary))
print(type(is_active))

"""
Write a Python program with these requirements:
1. Store "250" in a variable called total_amount.
2. Check its original data type.
3. Convert it into an integer.
4. Add 150 to the converted value.
5. Print the final result.
6. Print the final data type.
Expected output:
Original Value: 250
Original Type: <class 'str'>
Converted Value: 250
Converted Type: <class 'int'>
Final Amount: 400
Final Type: <class 'int'>

"""

total_amount="250"
print(f"Orginal value:{total_amount}")
print(type(total_amount))
total_amount=int(total_amount)
print(f"Converted value:{total_amount}")
total_amount+=150
print(f"Final Amount:{total_amount}")
print("Original Type:", type(total_amount))
print("Final Type:", type(total_amount))


"""
Day 3 – Type Conversion and Boolean

Write a Python program that:
1. Stores "45.75" in a variable called price.
2. Converts it into a float.
3. Stores "100" in another variable called quantity.
4. Converts it into an integer.
5. Calculates the total price (price × quantity).
6. Prints the total and its data type.
Expected output:
Price: 45.75
Quantity: 100
Total Price: 4575.0
Total Price Type: <class 'float'>
"""

price= "45.75"
converted_price=float(price)
print("Price:", converted_price)
quantity="100"
converted_quantity=int(quantity)
print("Quantity:", converted_quantity)
total_price=converted_price*converted_quantity
print("Total Price:", total_price)
print("Total Price Type:", type(total_price))

"""
Topic: Day 1 + Day 2 + Day 3 – Multiple concepts

Write a Python program using the following information:
employee_name = "Naasir"experience = "12"salary = "45000.50"is_active = "True"



Requirements:
1. Convert experience into an integer.
2. Convert salary into a float.
3. Convert is_active into a Boolean.
4. Print all converted values.
5. Print the data type of each converted variable.
Expected output:
Employee Name: Naasir
Experience: 12
Salary: 45000.5
Is Active: True

Data Types:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
"""

employee_name = "Naasir"
experience = "12"
salary = "45000.50"
is_active = "True"

converted_experience=int(experience)
converted_salary=float(salary)
converted_is_active=bool(is_active)
print(f"Employee Name: {employee_name}")
print(f"Experience: {converted_experience}")
print(f"Salary: {converted_salary}")
print(f"Is Active: {converted_is_active}")

"""
Topic: Day 1–3 – Combined coding challenge

Write a Python program using these values:
employee_name = "Naasir"experience = "12"salary = "45000.50"bonus = "5000"



Requirements:
1. Convert experience into an integer.
2. Convert salary into a float.
3. Convert bonus into a float.
4. Calculate total salary (salary + bonus).
5. Calculate average monthly salary by dividing total salary by 12.
6. Print employee name, experience, total salary and monthly average.
7. Print the data type of all calculated values.
Expected output:
Employee Name: Naasir
Experience: 12
Total Salary: 50000.5
Monthly Average: 4166.708333333333
"""
employee_name = "Naasir"
experience = "12"
salary = "45000.50"
bonus = "5000"

converted_experience=int(experience)
converted_salary=float(salary)
converted_bonus=float(bonus)
total_salary=converted_salary+converted_bonus
average_monthly_salary=total_salary/12
print(f"Employee Name: {employee_name}")
print(f"Experience: {converted_experience}")
print(f"Total Salary: {total_salary}")
print(f"Monthly Average: {average_monthly_salary}" )