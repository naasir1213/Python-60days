#Understanding if Statement
#The if statement executes a block of code only when the condition is True.

#Syntax:
#if condition:
    # block of code

#Example 1:

age=25

if age>=18:
   print("Elgible to vote")
print("Program Completed")

#What happens when the condition is False?
#Example:2
age=15
if age>=25:
   print("Elgible to vote")
print("Program Completed")  

# Python skips the indented block.
#  Python executes the next statement.

#Understanding Indentation
#Indentation is very important in Python
#Correct Indentation
age=25

if age>=18:
    print("Elgible")

#Incorrect Indentation
# age=25

# if age>=18:
# print("Elgible")

# The above Example produces produces an IndentationError because Python expects an indented block after the if statement.

# Topic 2:if-else Statements
'''
1. What is an if-else statement?
An if-else statement allows Python to make a decision between two possible outcomes.
- If the condition is True, the if block executes.
- If the condition is False, the else block executes.
'''

# Syntax
# if condition:
#     #Executes when condition is True
# else:
#     #Executes when condition is False

#Pratical example Odd or Even
number=10

if number%2==0:
    print("Even")
else:
    print("Odd")

"""
Problem: Positive or Negative Number

Write a Python program that:
1. Takes an integer stored in a variable called number.
2. Checks whether the number is greater than or equal to zero.
3. If True, print "Positive Number".
4. Otherwise, print "Negative Number".
Test cases:
Input	Expected output
10	Positive Number
-5	Negative Number
0	Positive Number
"""
number=0
if number>0:
    print("Positive Number")
elif number==0:
    print("Zero")
else:
   print("Negative Number") 

#Nested if statments in python
#A nested if means writing one if statement inside another if statement.
"""
In simple words, Python first checks an outer condition. If that condition is True, it enters the outer block and checks another condition inside it.
Real-world example
Imagine a student applying for an examination.

There are two conditions:
1. Student must be at least 18 years old.
2. Student must have completed registration.
Only when both conditions are satisfied can the student attend the examination.

Syntax

if condition1:
    if condition2:
        #Execute when both conditions are true
    else:
       #Inner condition is False
 else:
     #Outer condition is False
     """

#Example
age=25
registration_completed=True

if age>=21:
    print("Age requirement Satisfied")
    if registration_completed:
        print("You are elgible for the examination")
    else:
        print("Please complete your registarion")
else:
    print("You are not elgible due to age")         

"""
Problem: Student Grade Eligibility

Write a Python program using nested if statements.

Requirements:
1. Store the student's age in age.
2. Store the examination score in score.
3. First check whether the student is 18 or above.
4. If age is eligible, check whether the score is greater than or equal to 50.
5. If both conditions are satisfied, print "Eligible for admission".
6. If age is eligible but score is below 50, print "Not eligible due to score".
7. If age is below 18, print "Not eligible due to age".
Use these test cases:
Age	Score	Expected output
22	75	Eligible for admission
22	40	Not eligible due to score
16	80	Not eligible due to age
16	30	Not eligible due to age

"""
age=18
score=51

if age>=18:
#    print("Age requirement is satisfied")
   if score>=50:
       print("Elgible for admission")
   else:
      print("Not elgible due to score")
else:
    print("Not elgible due to age")    

#5.Multiple conditions using logical operators
"""
We will combine conditional statements with:
- and
- or
- not
These operators help us evaluate multiple conditions together.
"""
#Example
age=25
salary=50000
if age>=18 and salary>=30000:
   print("Elgible")
else:
    print("Not Elgible")

#Logical Operators
"""
Logical operators allow us to combine multiple conditions and evaluate them together.

Python provides three logical operators:
1. and
2. or
3. not
Let's understand each one with examples.
"""
#AND Operator Example

age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Eligible")
else:
    print("Not Eligible")


#OR Operator

#The or operator returns True when at least one condition is True.
#Example
age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Access Granted")
else:
    print("Access Denied")

#NOT Operator
#not operator reverse the boolean result
#not True becomes False
#not Falase becomes True

#Example
is_blocked = False

if not is_blocked:
    print("Account is active")
else:
    print("Account is blocked")

"""
Why?
1. is_blocked is False.
2. not is_blocked becomes True.
3. Python executes the if block.
NOT truth table
Condition	Result
True	False
False	True
"""


#6.Short Circuit Evaluation
#Python sometimes stops evaluating conditions once the final result is already determined.
#With AND
 
 # result =False and True
 # Python knows the result must be False, so it doesn't need to evaluate the second operand.

 # With OR
#  result = True or False

 #Python knows the result must be True, so it doesn't need to evaluate the second operand.

# Problem:Employee Elgibility
"""
Write a Python program using logical operators.

Requirements:

An employee is eligible for a bonus if:
- Experience is greater than or equal to 3 years.
- Salary is greater than or equal to ₹30,000.
If both conditions are satisfied, print:

Eligible for Bonus

Otherwise, print:

Not Eligible for Bonus
"""
experience=3
salary=30000

if experience>=3 and salary>=30000:
   print("Elgible for Bonus")
else:
    print("Not Elgible for Bonus")

#OR Practical Example
"""
Imagine a student can participate in a competition if:
- Their score is greater than or equal to 90, OR
- They have won a district-level competition.
"""
score = 85
district_winner = True

if score >= 90 or district_winner:
    print("Eligible for Competition")
else:
    print("Not Eligible for Competition")

"""
Problem: Free Delivery Eligibility

An online shopping application provides free delivery if either of these conditions is satisfied:
1. Order amount is greater than or equal to ₹1,000.
2. Customer is a premium member.
Otherwise, delivery charges apply.

Write a Python program using the or operator.
"""
order_amount=1000
is_a_premium_member=False

if order_amount>=1000 or is_a_premium_member:
    print("Free Delivery")
else:
    print("Charges Apply")    


"""
Problem: User Account Status

Consider the following requirements:
- If the user account is NOT blocked, print "Account is Active".
- Otherwise, print "Account is Blocked".
"""
is_blocked=True

if not is_blocked:
    print("Account is Active")
else:
    print("Account is Blocked")

#Topic 7:Conditional Expressions (Ternary Operator)
#Python provides a way to write conditional statements in a single line using the ternary operator.

#Syntax
# variable = value_if_true if condition else value_if_false
age=25

result="Eligible for Vote" if age>=18 else "Not Eligible"
print(result)

#Even or odd
number=21
result="Even" if number%2==0 else "Odd"
print(result)

"""
Write a Python program to determine whether a person is eligible for a loan.

Requirements:

A person is eligible for a loan if BOTH conditions are satisfied:
1. Age must be greater than or equal to 21.
2. Monthly salary must be greater than or equal to ₹25,000.
Otherwise, print "Loan Not Approved".

Use the following input:
age = 25
monthly_salary = 30000
"""
age = 25
monthly_salary = 30000

if age>=21 and monthly_salary>=25000:
   print("Loan Approved")
else:
   print("Loan Not Approved")

"""
Coding Challenge: Grade Calculation
10 Marks
Now let's test your understanding of if-elif-else.
Problem statement
Write a Python program to calculate a student's grade based on marks.
Marks	Grade
90–100	A
75–89	B
60–74	C
50–59	D
Below 50	Fail
"""
marks = 82

if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=90 :
       print("Grade A")
elif marks>=75:
      print("Grade B")
elif marks>=60:
      print("Grade C")
elif marks>=50:
      print("Grade D")
else:
      print("marks is below 50")

#Nested if +Logical Operators
"""
Problem: Employee Promotion Eligibility
An employee is eligible for promotion if:
1. Experience is greater than or equal to 5 years.
2. Performance rating is greater than or equal to 4.
Additional requirement:
- First check whether experience is at least 5 years.
- Inside that condition, check the performance rating using a nested if.
- If experience is below 5, print "Insufficient Experience".
Use this input:
experience = 6
performance_rating = 4.5
"""
experience = 7
performance_rating = 5

if experience>=5:
   if performance_rating>=4:
      print("Eligible for Promotion")
   else:
      print("Not Eligible for Promtion")
else:
    print("Insufficient Experience")      


# A developer wants to check whether a number is between 10 and 50.

number = 35

if number >= 10 and number <= 50:
    print("Number is within range")
else:
    print("Number is outside range")

# Remember: When checking whether a number falls within a range, both boundaries must be satisfied.

"""
Problem: Electricity Bill Calculation
Write a Python program to calculate an electricity bill based on units consumed.
Requirements
Units consumed	Rate per unit
0–100	₹2
101–200	₹3
201–300	₹5
Above 300	₹7

For this exercise, apply the applicable rate to all units consumed (slab selection, not progressive billing).

Additional requirements:
- If units are negative, print "Invalid Units".
- Otherwise, calculate the bill using if-elif-else.
Test input
units=250
"""
units=250

if units<0:
    print("Invalid Inputs")
elif units<=100:
    print("Calculate the bill:" , units*2)
elif  units<=200:
    print("Calculate the bill:", units*3)
elif  units<=300:
    print("Calculate the bill:", units*5)
else:
    print("Calculate the bill:", units*7)