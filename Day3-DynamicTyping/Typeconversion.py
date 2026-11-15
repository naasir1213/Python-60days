#There are two types of Type conversion in Python:
#1. Implicit Type Conversion:Python automatically converts one data type to another without any user involvement. This is also called Type Casting.
#2. Explicit Type Conversion: The user converts the data type of an object to another data

#Implicit type conversion example
a=10
b=15.5
result=a+b
print(result)
print(type(result))

#Explicit type conversion
"""
Function	Converts into	Example
int()	Integer	int("25")
float()	Float	float("25.5")
str()	String	str(100)
bool()	Boolean	bool(1)
list()	List	list("abc")
tuple()	Tuple	tuple([1, 2])
set()	Set	set([1, 2, 2])

"""
status="False"
print(bool(status)) #True.  Because the string is not empty.

#Collection Conversions
#String to list
print(list("Naasir"))
#List to Tuple
tuple([1,2])
print(tuple)
#List to set
set([10,20,30])
print(set)

#Type Conversion errors
#Five important errors
#1. Value Error
age="10"
print(int(age))  //Value Error

#2.TypeError
age="35"
print(age+35) //TypeError

#3.ZeroDivisionError
a=10
b=0
print(a/b) //ZeroDivisionError

#4.TypeError with None
response=None
print(int(response)) #None can't be directly converted into an int

#5.Type Error with incompatible comparsion
actual_status="200"
expected_status=200

print(actual_status==expected_status) #False

#Correct approach
print(int(actual_status)==expected_status)  //True

#Coding Practice
#1.Predict the output of each program.

a = "100"
b = 50

a = int(a)

result = a + b

print(result)
print(type(result))


  
