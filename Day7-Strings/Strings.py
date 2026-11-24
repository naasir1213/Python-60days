"""
1.What is String?
A string is a sequence of characters enclosed within quotation marks
Characters can include
. Alphabets
.Numerics
.Special Characters
.Spaces
.Symbols
Example
name="Naasir"
company="Google"
message="Welcome to python"
name,company and message are string  variables

Important:Even if we store number inside the quotation marks python will treat as strings
"""
age="30"
# age=int(age)
salary=50000
print(type(age))
print(type(salary))

"""
2.Types of String Declaration
Python supports three common ways to declare strings
A.Single Quotes
name='Python'
print(name)
B.Double Quotes
name="Python"
print(name)
C.Triple Quotes
Triple quotes allow multiline strings
"""
message="""Welcome to Python.
Today we are learning strings.
Python is easy to learn"""
print(message)

# 3.Quotes inside strings
message="It's a beautiful day"
print(message)

#4.Understanding string length
#Python provides built-in len() function to calculate the number of characters in a string

name="python  "
print(len(name))
#Note:Spaces are also counted as characters

#Example-1
employee_name="naasir"
employee_id="emp1025"
department="Quality Engineering"

print(employee_name)
print(type(employee_id))
print(len(employee_name))
print(len(department))
print(len(employee_id))
print("======================")

message = "Python Programming"

print(len(message))
print(len(message.strip())) #strip() removes leading and trailing whitespace.
print(type(len(message)))
#Note:strip() removes spaces only at the beginning and end, not spaces in the middle.

print("================")

message = "  Python  "

print(len(message))
print(len(message.strip()))
print(type(message.strip()))

print("=================")

#String Indexing
#Positive Indexing
language="PYTHON"

print(language[0])
print(language[2])

print("===============")

#2.Negative Indexing
language = "PYTHON"

print(language[-1])
print(language[-3])
# print(language[-7]) #Index out of range
print("=============")

# If the first statement raises an exception, Python normally stops executing the remaining statements in that program unless the exception is handled.

employee_name = "MOHAMMAD"

print(employee_name[0])
print(employee_name[-1])
print(employee_name[3])
print(employee_name[-2])
print(employee_name[-8])

print("===============")

#3.String Slicing-We will learn how to extract multiple characters from a string
#Syntax
#string[start:end:step]
language="PYTHON"
print(language[0:3])
print(language[0:2])
print(language[2:5])
print(language[1:4])
print("==================")
#Rule:Start index is included, but end index is excluded.

language = "PYTHON"

print(language[:3]) #Python assumes the starting index is 0.
print(language[2:]) # THON Python continues from index 2 until the end of the string.
print(language[:])#Python extracts the entire string.

print("==============")
#Slicing with Step
# Syntax
# string[start:end:step]
#The step parameter determines how many positions Python moves each time.

language = "PYTHON"

print(language[0:6:1])
print(language[0:6:2])
print(language[::2])
print("===========")
language = "PYTHON"

print(language[::2]) #Python starts at index 0 and moves two positions each time.
print(language[1::2]) # Python starts at index 1 and moves two positions each time.
print(language[::-1]) # [::-1] is a common Python technique for reversing a string.
print("============")

company = "MICROSOFT"

print(company[1:7:2])
#Selected indexes: 1 → 3 → 5
print(company[-1:-6:-1])
#Selected indexes: -1 → -2 → -3 → -4 → -5
print(company[::3])
#Selected indexes: 0 → 3 → 6
print(company[::-2])
#Selected indexes: 8 → 6 → 4 → 2 → 0
print("===============")
"""
Remember these two rules:
- Negative step (-1) means move backwards.
- Negative step (-2) means move backwards, skipping one character between selections.
"""

"""
Write Python statements to:
1. Extract the first name (MOHAMMAD).
2. Extract the last name (NAASIR).
3. Reverse the complete employee name.
4. Extract every second character from the complete name.
5. Extract the first four characters using slicing.
"""
employee_name = "MOHAMMAD NAASIR"
print(employee_name[0:8])
print(employee_name[9:15])
print(employee_name[::-1])
print(employee_name[0:15:2])
print(employee_name[0:4])
print("=============")

#String Immutability
# name="Python"
# name[0]="J" 
# print(name) #TypeError
# Python strings are immutable, meaning once a string is created, its individual characters cannot be changed.
# If you want JYTHON, create a new string:

name = "PYTHON"

name = "J" + name[1:]

print(name)

print("====================")
# Notice that we didn't modify the original string character. 
# We created a new string and reassigned it to name.

"""
Are Python strings mutable or immutable?

Answer: Python strings are immutable.
 Once a string is created, its individual characters cannot be modified. If we need to change a string, we must create a new string.
"""
name = "PYTHON"

name = name.replace("P", "J")

print(name)
print("==============")
#replace doesnt modify the existing string
#It returns a new string
# Remember: String methods generally return new strings rather than modifying the original string.

name = "python"

result = name.upper()

print(name)
print(result)

name = name.replace("p", "J")

print(name)
print("==============")

#Python String Operators
"""
Operator	Purpose
+	Concatenation (joining strings)
*	Repetition
in	Membership checking
not in	Negative membership checking
"""
#Example
first_name="Naasir"
last_name="Mohammad"
print(first_name + " " + last_name)
print("Python" *3)
print("Py" in "Python")
print("Java" not in "Python")
print(name == "python")
print(name != "Python")
print("P" in name)
print("z" not in name)
print("==================")
company = "Google"
role = "QA"
print(company+role) #GoogleQA
print(role * 3)
print("oo" in company)
print("z" not in company)
print("Google" == company) #Google and company contain exactly the same string
print("Google" != company)
print("============")

#6.String Methods
"""
Method	Purpose
upper()	Converts to uppercase
lower()	Converts to lowercase
capitalize()	Capitalizes the first character
title()	Capitalizes the first letter of each word
strip()	Removes leading and trailing whitespace
lstrip()	Removes leading whitespace
rstrip()	Removes trailing whitespace
replace()	Replaces a substring
count()	Counts occurrences of a substring
"""
message="  hello python world  "
print(message.upper())
print(message.lower())
print(message.capitalize())
#Output is:hello python world  
"""
Important behaviour of capitalize():
1. It converts the first character of the string to uppercase.
2. It converts all remaining characters to lowercase.
3. It does not remove leading or trailing spaces.
Here, the first character is a space, not h.

Therefore, capitalize() doesn't capitalize the h.
"""
print(message.title())
print(message.strip())
print(message.replace("python", "java"))
print("================")
#Note:These methods return new strings.They do not modify the original string
text = "python programming"

print(text.upper())
print(text.capitalize())
print(text.title())
print(text.count("m"))
print(text.replace("python", "Java"))
print("============")

message=message = "hello python"
message = message.upper()
print(message)
#Here it will not modify the original string.create a new string so we need to store in a variable
"""
Interview concept
This is related to string immutability.
Python strings are immutable.
 String methods such as upper(), lower() and replace() return new strings rather than modifying the original string.
"""
#Searching Methods
"""
find() – returns the index of the first occurrence; returns -1 if not found.
index() – returns the index of the first occurrence; raises ValueError if not found.
startswith() – checks whether a string starts with a given value.
endswith() – checks whether a string ends with a given value.
"""

text="Python programming"

print(text.find("P"))
print(text.find("gram"))
print(text.find("Java"))
print("===========")

#Difference between find and Index
#text = "Python programming"

print(text.find("Java")) #-1
#print(text.index("Java")) #Value Error
#find("Java") returns -1.
#index("Java") raises ValueError: substring not found.
text = "Python programming"

print(text.find("o"))
print(text.find("m"))
print(text.find("Java"))
print(text.startswith("Py"))
print(text.endswith("ing"))

text = "Python programming"

if text.find("Java"):
    print("Java found")
else:
    print("Java not found")

print("==============")

"""
Step by step:
1. text.find("Java") searches for "Java".
2. Since "Java" is not present, find() returns -1.
3. In Python, -1 is a truthy value.
4. Therefore, the if condition executes.
"""
if text.find("Java") != -1:
    print("Java found")
else:
    print("Java not found")

print("===========")

"""
Important interview concept
Value	Boolean evaluation
0	False
-1	True
1	True
None	False
"""
text = "Python programming"

if text.find("Python"):
    print("Found")
else:
    print("Not Found")

print("===========")
"""
find("Python") searches for "Python".



"Python" starts at index 0.
Therefore, find() returns 0.
Python treats 0 as False.
So the else block executes.

find() result	Boolean value
0	False
1	True
5	True
-1	True
Interview tip: Never directly use find() as an if condition when checking whether a substring exists. Use:
if text.find("Python") != -1:
Or
if "Python" in text:
    """

#Split and Join
#Convert between strings and lists

#1.Split()-Converts a string into a list
message="Python is easy to learn"
result=message.split()
print(result)
print(type(result))

print("===========")

#2.Split using a comma
data="apple,banana,Orange"
result= data.split(",")
print(result)

print("============")

#3.Join-Converts a list into string
# join() combines strings from an iterable (commonly a list) into one string, using the specified separator.

fruits=["apple", "banana", "orange"]
result=" ".join(fruits)
print(result)
print("============")
#Other separators
fruits = ["apple", "banana", "orange"]
print(",".join(fruits))
print("-".join(fruits))
print("".join(fruits))

print("============")

"""
Important Difference
Method	Input	Output
split()	String	List
join()	Iterable of strings	String

Important: join() requires all elements to be strings. If a list contains integers, it raises a TypeError.

"""
message="Python is very powerful"

words= message.split()
print(words)
print(len(words))
print(words[0])
print(words[-1])
print(type(words))

print(len(message))

print("=====================")

# len(message) counts characters, including spaces.
# len(message.split()) counts words because split() returns a list.

#Join
fruits=["apple", "banana", "orange"]
print(" ".join(fruits))
print(",".join(fruits))
print("-".join(fruits))
print("".join(fruits))

print("===================")

#Debugging challenge
"""
Find the issue in the  code
# numbers=[10,20,30,40,50]
# result=",".join(numbers)
# print(result)

TypeError: sequence item 0: expected str instance, int found
join() expects string elements.
Our list contains integers.
Python cannot directly join integers into a string.
"""
numbers=[10,20,30,40,50]
result=",".join(str(num) for num in numbers)
print(result)
print(type(result))

print("===================")
numbers = [2, 4, 6]
result = ":".join(str(num + 5) for num in numbers)
print(result)

print(type(result))

print("===============")

#String formatting and f strings
#An f string allows us to insert variables directly inside {}
name="Naasir"
experience=12
print(f"My name is {name}")
print(f"I have {experience} years of experience")
print("================")
# We can perform the calculations inside the {}
a=10
b=20
print(f"Sum of:{a+b}")
print("=============")

employee="Naasir"
salary=50000
bonus=5000

print(f"Employee:{employee}")
print(f"Salary:{salary}")
print(f"Total:{salary+bonus}")
print(f"Bonus:{bonus*2}")

print("====================")

#Note:f-strings allow us to place variables and expressions directly inside {}

#Formatting numbers using f-strings
#Example 1-Thousands separator
salary=500000
print(f"salary:{salary:,}")

#Example-2-Decimal Precision
price=125.71998
print(f"Price:{price:.2f}")
#.2f display the two digits after the decimal point
#Example-3:Percentage
percentage=0.856787
print(f"Score:{percentage:.2%}")
print("===================")

price=1234.5678
quantity=3
total=price*quantity
print(f"Price:{price:.2f}")
print(f"Total:{total:2f}")
print(f"Total with separator:{total:,.2f}")
print("===================")

"""
Remember these formatting rules
- :.2f → Two decimal places.
- :,.2f → Thousands separator and two decimal places.
- :.2% → Percentage with two decimal places.
"""
score = 0.87654
amount = 250000

print(f"Score: {score:.1%}")
print(f"Amount: {amount:,}")
print(f"Amount: {amount:,.2f}")

"""
Important clarification
For discount = 0.10:
- .0% → 10%
- .1% → 10.0%
- .2% → 10.00%
For currency formatting, remember that the comma separates thousands, not decimal digits.
"""
price = 2000
discount = 0.15

final_price = price - (price * discount)

print(f"Discount: {discount:.0%}")
print(f"Final Price: {final_price:,.2f}")

print("===================")

#String formatting
#Write a python program using these variables
product_name="Laptop"
price=55000
discount=0.12
discount_amount=price*discount
final_price=price-discount_amount

print(f"Discount:{discount_amount:.0%}")
print(f"Final Price:{final_price}")
print(f"ProductName:{product_name}")
print(f"OrginalPrice:{price:,.2f}")
print(f"FinalPrice:{final_price:,.2f}")

print("===================")

discount = 0.12
discountamount = 6600
finalprice = 48400

print(f"Discount:{discount:.0%}")
print(f"DiscountAmount:{discountamount:,.2f}")
print(f"FinalPrice:{finalprice:,.2f}")

print("====================")

employee_name = "  naasir mohammad  "
clean_name=employee_name.strip()
print(clean_name)
title_result=clean_name.title()
print(title_result)
print(len(clean_name))
words=clean_name.split()
result=("-").join(words)
print(result)

print(f"finalstring:{title_result}")

print("====================")

#String methods and searching
text = "Python programming"

print(text.count("m"))
print(text.find("gram"))
print(text.find("Java"))
print(text.startswith("Py"))
print(text.endswith("Python"))

print("=================")

#Split(),join() and data types
message="Python is easy"
words  = message.split()
print(words)
print(words)
print(len(words))
print("-".join(words))
print(type("-".join(words)))

print("====================")

price = 2500.567
quantity = 2
discount = 0.10

total = price * quantity
final_price = total - (total * discount)

print(f"Total: {total:,.2f}")
print(f"Discount: {discount:.0%}")
print(f"Final Price: {final_price:,.2f}")
print("=============")

employee = "  MOHAMMAD NAASIR  "

clean_naming= employee.strip()
print(clean_naming)
print(clean_naming.lower())
title_case=clean_naming.title()
print(title_case)
print(len(clean_naming))
print(clean_naming.startswith("MOH"))
print(f"FinalNameAfterRemovingSpaces:{title_case}")

print("=================")

# String methods and Immutability

text = "hello python"

result1 = text.upper()
result2 = text.replace("python", "world")
result3 = text.capitalize()

print(text)
print(result1)
print(result2)
print(result3)
print(len(text))

print("===================")

message = "  python programming is interesting  "

remove_spaces=message.strip()
print(remove_spaces)
title_case=remove_spaces.title()
print(title_case)
print(len(remove_spaces))
words=remove_spaces.split()
print(words)
print(remove_spaces[::-1])
print("python" in remove_spaces)
print("_".join(words))
print(f"Final Summary:{title_case}")