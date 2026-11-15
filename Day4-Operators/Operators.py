#What is Operators in Python?
#Operators are special symbols that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
#Example
a=10
b=5
result=a+b
print(result)

#Important concept to understand
#Division
a=10
b=2
print(a/b) # It returns as float
#Remember: The / operator returns a float, even when the division result is a whole number.
print(type(a/b))

#Floor division
print(10//3)
print(15//4)
#Floor division rounds down to the nearest integer, not simply towards zero.

#Modulus
print(10%5)
print(10%3)

#Modulus returns the remainder after division.

#Important interview question:Even or odd
num=10
if num%2==0:
   print("Even Number")
else:
   print("Odd Number")

#Exponentiation(**)
#Used to calculate powers

print(2**3)
print(5**2)

#Example
a=17
b=5
print(a/b)  # 3.4
print(a//b) #3
print(a%b)  #2

"""
Problem 1: Arithmetic Operations

Write a Python program that:
1. Declares two variables: a = 25 and b = 4.
2. Performs addition.
3. Performs subtraction.
4. Performs multiplication.
5. Performs division.
6. Performs floor division.
7. Finds the remainder.
8. Calculates the power of a raised to b.
Expected output:
Addition: 29
Subtraction: 21
Multiplication: 100
Division: 6.25
Floor Division: 6
Modulus: 1
Exponentiation: 390625
"""

a=25
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Comparision Operators
"""
Comparison operators compare two values and return a Boolean result: True or False.
Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
"""
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

"""
Declare two variables:
x = 50
y = 30

Write six comparison statements using all six comparison operators.
"""
x = 50
y = 30
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

"""
Logical operators
Python has three logical operators:
Operator	Meaning
and	True when both conditions are True
or	True when at least one condition is True
not	Reverses the Boolean result
"""
#AND
# age=25
# salary=50000
# print(age>18 AND salary >30000)

#OR
# age = 16
# salary = 50000

# print(age > 18 or salary > 30000)

#NOT
# is_active = True

# print(not is_active)

#Short Circuit Evaluation
#AND
# If the first condition is False, Python doesn't need to evaluate the second condition.

print(False and True) # False

#OR
#If the first condition is True, Python doesn't need to evaluate the second condition.
print(False or True)

"""
Assignment operators
Assignment operators are used to assign or update variable values.
Operator	Example	Equivalent operation
=	       x = 10	Assign 10
+=	       x += 5	x = x + 5
-=	       x -= 5	x = x - 5
*=	       x *= 2	x = x * 2
/=	       x /= 2	x = x / 2
//=	       x //= 2	x = x // 2
%=	       x %= 3	x = x % 3
**=        x **= 2	x = x ** 2
"""
x=10
x+=5
print(x) #15
x*=2
print(x) #30
x-=5
print(x) #25

"""
Membership operators
Python provides two membership operators:
Operator	Meaning
in	      Checks whether an element exists in a sequence
not in	   Checks whether an element does not exist in a sequence

These operators are commonly used with strings, lists, tuples, sets and dictionaries.
"""
#Example Using in
fruits=["apple","banana","mango"]
print("apple" in fruits)
print("Strawberry" in fruits)

#Example: Using not in
Cars=["Honda","Toyota","Fortuner"]
print("i20" not in Cars)
print("Honda" not in Cars)

# Important interview concept: Dictionary membership
# When using in with a dictionary, Python checks the keys, not the values.

employee={
    "name":"Naasir",
    "experience":12
}
print("name" in employee)
print("department" in employee)
print("Naasir" in employee.values())

#Exercise
numbers = [10, 20, 30, 40, 50]

print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)
print(100 not in numbers)

name = "Python Programming"

print("Python" in name)
print("Java" not in name)

#Identity Operators
"""
Python provides two identity operators:
- is
- is not
Important difference:
- == checks whether two objects have equal values.
- is checks whether two references point to the same object in memory.
"""
#Example 1:Equal values
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, because the values are equal
print(a is b)  # False, because they are different objects in memory

a=[10,20,30]
b=a
print(a==b)
print(a is b) 
# Here, b = a means both variables refer to the same list object.

#Bitwise Operators
a=5
b=3
print(a&b)

#Binary Representation
print(bin(5))
print(bin(3))

#The prefix 0b indicates that the number is represented in binary.

print(5|3)

#XOR
a=6
b=3
print(a^b)

#Binary Representation
#6=110
#3=011

#AND (&) → Returns 1 only when both bits are 1.
#XOR (^) → Returns 1 only when both bits are different.

#Bitwise Not
#0 becomes 1
#1 becomes 0
a=8
print(~a)
#Formula
#  ~n=-(n+1)

#Operator Precedence

result=10+5*2
print(result)

"""
Python operator precedence
Here is the priority order you should understand:
Priority	Operator	Description
1	()	Parentheses
2	**	Exponentiation
3	+x, -x, ~x	Unary operators
4	*, /, //, %	Multiplication and division
5	+, -	Addition and subtraction
6	<<, >>	Bitwise shifts
7	&	Bitwise AND
8	^	Bitwise XOR
9	\|	Bitwise OR
10	Comparisons, in, is	Comparison operators
11	not	Logical NOT
12	and	Logical AND
13	or	Logical OR
"""

#Exercise
print(10 + 2 * 5) # 20
print((10 + 2) * 5) # 60
print(20 / 5 + 2) # 6.0 #Division has higher precedence than addition
print(2 ** 3 * 2) # 16

#When operators have the same precedence, Python evaluates them from left to right. For example, in the expression 10 - 5 + 2, both subtraction and addition have the same precedence, so Python evaluates them from left to right, resulting in 7.
print(10 - 5 + 2) # 7
print(10 - (5 + 2)) # 3
print(20-5-3)#12
#However, exponentiation is right-associative:
print(2 ** 3 ** 2) #512