#A Loop is used to execute a block of code repeatedly
#Python provides two primarly types of loops
#For Loop and While Loop
#Example
for i in range(1,6):
    print(i)

print("===================")
#Whil loop:Executes a block of code repeatedly as long as the given condition is true
#Print numbers from 1 to 5
i=1
while(i<=5):
 print(i)
 i=i+1

print("============")
#Example:Print even numbers from 2 to 20 using a while loop
i=2
while(i<=20):
   print(i)
   i=i+2

print("============")

#Example:Calculate the sum of numbers from 1 to 10 using a while loop

sum=0
i=1
while(i<=10):
     sum=sum+i
     i=i+1
print("Sum of numbers:",sum)

#Write a program using a while loop to calculate the sum of all even numbers between 1 and 20
sum=0
i=2
while(i<=20):
    sum=sum+i
    i=i+2
print("Sum of even numbers between 1 and 20:",sum)

print("=================")

"""
For Loop:Is used to iterate over a sequence or iterable,such as:
List
String
Tuple
A range o numbers
Syntax
for variable in sequence
Statements
"""

"""
When would we use a while loop instead of for loop?
When the number of iterations is not known in advance and execution depends on a condition
"""
"""
Understanding the range function
Python provides 3 ways to use range()
range(5)  -->means(0,4)
range(1,6) --->means(1,5)
range(1,10,2)--->means(1,3,5,7,9)

#Step can be negative
range(10,0,-1) -->means(10,9,8,7,6,5,4,3,2,1)
"""

#Print numbers from 20 to 1 in reverse order using a for loop
for i in range(20,0,-1):
    print(i)

print("====================")

"""
Break,Continue and Pass
These are called loop control statements

Statement-------------------- Purpose
break   ---------------------Immediately terminates the loop
continue--------------------- skip the current iteration and moves to the next
pass   --------------------- Does nothing

"""
#Example:
for i in range(1,6):
    if(i==4):
       break
    print(i)   

print("==================")

#Continue Example

for i in range(1,6):
    if i==3:
      continue
    print(i)
print("=============")

#Example: Pass Statement:Pass statement is a null operation.It does nothing when executed
for i in range(1,6):
    if i==3:
       pass
    print(i)
print("=================")

#Example of combined
for i in range(1,6):
    if i==3:
       break
    elif i==2:
       continue
    print(i)

print("==================")


"""
Can we use both break and continue inside the same loop?
Yes. We can use both statements in the same loop based on different conditions. continue skips an iteration, whereas break terminates the loop.
"""

#Nested Loops:A nested loop means placing one loop inside another loop.
# The inner loop completes all its iterations for every single iteration of the outer loop.
#Example
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

print("================")
"""
Outer loop executes 3 times.
Inner loop executes 3 times for each outer iteration.
Total inner-loop executions = 3 × 3 = 9.
"""

#Multiplication table structure
for i in range(1,3):
    for j in range(1,4):
        print(i,j)
#Notice that when i = 1, all three values of j execute before i becomes 2.
print("==================")

# Write a Python program using nested for loops to print this output:
# Use an outer loop to run 2 times and an inner loop to print * 3 times in each outer iteration.

for i in range(1,3):
    for j in range(1,4):
        print("*")

print("===========")

"""
Write a nested loop program to print this output:
1 2 3
1 2 3
1 2 3
"""
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()
print("==============")
#Write a program using nested loops to generate right-angled-triangled pattern

for i in range(1,5):
    for  j in range(1,i+1):
        print("*", end=" ")
    print()
print("=================")

for i in range(5,1,-1):
    for  j in range(1,i+1):
        print("*", end=" ")
    print()

print("==================")

#Write a nested loop program to print
"""
1
1 2
1 2 3
1 2 3 4
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j , end=" ")
    print()
print("===========")

"""
Write a program for below output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("============")

"""
Print below pattern
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()

print("==============")

for i in range(1, 5):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print("================")

#Note:In nested-loop pattern problems, we can use the outer loop variable to dynamically control the inner loop's iteration count. This allows us to create increasing or decreasing patterns.

#Write a Python program using a while loop to calculate the factorial of a number.

#Exmaple=5
i=1
fact=1
while(i<=5):
    fact=fact*i
    i=i+1
print(fact)

print("====================")


#Factorial is the product of all positive integers from 1 to a given number. We initialize the accumulator to 1 and use a while loop to multiply each number until the given number is reached."

i = 1
total = 0

while i <= 5:
    total =total+i
    i=i+1
print("Total of:",total)
print("==============")

#Write a Python program using a for loop to calculate the sum of all odd numbers between 1 and 20.
total=0
for i in range(1,20,2):
    total=total+i
print("Total odd numbers:",total)
print("====================")

for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("=============")

for i in range(1, 6):
    if i == 3:
        continue
    elif i == 5:
        break
    print(i)
else:
    print("Loop completed")
print("============")

#Write a Python program using nested loops to print this pattern:
"""
Output
1
2 3
4 5 6
7 8 9 10
"""
num=0
for i in range(1,5):
    for j in range(1,i+1):
        num=num+1
        print(num, end="")
    print()
print("=====================")

for i in range(1, 4):
    for j in range(i, 4):
        print(j, end=" ")
    print()
print("==========")

for i in range(5, 1, -1):
    for j in range(1, i):
        print("*", end=" ")
    print()
print("====================")
total = 0

for i in range(1, 6):
    for j in range(1, i + 1):
        total = total + j

print(total)
print("================")
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue
        print(i, j)
    else:
        print("Inner loop completed")
print("================")

total = 0

for i in range(1, 5):
    total = total + i
    print(total, end=" ")

print("\nFinal Total:", total)
print("============")

for i in range(10, 0, -2):
    print(i, end=" ")

    if i == 4:
        break

print("==============")
total = 0

for i in range(1, 6):
    if i == 3:
        continue

    total = total + i

print(total)

print("============")
for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 4:
            continue

        print(i + j, end=" ")

    print()
print("=========")

#An empty print() statement prints a newline because Python's default end value is "\n".
i = 1
total = 0

while i <= 5:
    total = total + i

    if total >= 6:
        break

    i = i + 1

print("i =", i)
print("total =", total)
print("===========")

total = 0

for i in range(1, 4):
    for j in range(1, 4):
        total = total + i * j

    print(total)
print("=============")
for i in range(1, 4):
    for j in range(1, 5):
        if j == 3:
            break

        print(i, j, end=" ")

    print()

print("================")

for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 5:
            break
        print(i, j)
    else:
        print("Inner loop completed")

print("Program completed")
print("===========")

for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 5:
            continue
        print(i, j)
    else:
        print("Inner loop completed")

print("Program completed")
print("===============")

for i in range(1, 4):
    for j in range(1, 5):

        if j == 2:
            continue

        if i == 3 and j == 3:
            break

        print(i, j, end=" ")

    else:
        print("Completed")

    print()
print("==============")
count = 0

for i in range(1, 4):
    for j in range(1, 4):

        if i == j:
            continue

        count = count + 1

    print("Count:", count)

print("Final Count:", count)

print("=================")
for i in range(1, 4):
    count = 0

    for j in range(1, 4):
        if i == j:
            continue
        count += 1

    print("Count:", count)
    
print("===============")

total = 0

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue

        total = total + 1

    print("Total:", total)

    total = 0

print("=================")
total = 0

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue

        total = total + 1

    print("Total:", total)

print("===============")
total = 0

for i in range(1, 4):
    for j in range(1, i + 1):
        if j == 2:
            continue

        total = total + i

    print("Total:", total)
print("==============")

total = 0

for i in range(1, 4):
    for j in range(1, i + 1):
        if i == j:
            continue

        total = total + j

    print("Total:", total)
print("============")
total = 0

for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 4:
            break

        total = total + j

    print("Total:", total)

print("===============")

total = 0

for i in range(1, 4):
    for j in range(1, 5):

        if j == 2:
            continue

        if i + j == 5:
            break

        total = total + i * j

    print("Total:", total)
print("=============")
total = 0  # Outside both loops

for i in range(1, 5):
    for j in range(1, 5):

        if i == j:
            continue

        if i + j > 5:
            break

        total = total + i + j

    print("i =", i, "Total =", total)