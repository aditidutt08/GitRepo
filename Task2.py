# Question 1: Write a program in Python to perform the following operation:
# 1. If a number is divisible by 3 it should print “Consultadd” as a string
# 2. If a number is divisible by 5 it should print “Python Training” as a string
# 3. If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.
# Answer: 
# a = int(input("Enter the value of a : "))
# if (a%3 == 0) and (a%5 == 0):
#     print("Consultadd - Python Training")
# elif (a%3 == 0):
#     print("Consultadd")
# elif (a%5 == 0):
#     print("Python Training")


# Question 2: Write a program in Python to perform the following operator based task:
# 1. Ask user to choose the following option first:
#   1. If User Enter 1 - Addition
#   2. If User Enter 2 - Subtraction
#   3. If User Enter 3 - Division
#   4. If User Enter 4 - Multiplication
#   5. If User Enter 5 - Average
# 2. Ask user to enter two numbers and keep those numbers in variables num1 and num2
#   respectively for the first 4 options mentioned above.
# 3. Ask the user to enter two more numbers as first and second for calculating the average as
#   soon as the user chooses an option 5.
# 4. At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.
# Answer: 
# num = int(input("Enter the value of between 1 to 5 : "))
# print("You entered the number: ", num)
# if (num==1) or (num==2) or (num==3) or (num==4):
#     num1 = int(input("Enter the first number : "))
#     num2 = int(input("Enter the second number : "))
#     if num==1:
#         result = num1 + num2
#     elif num==2:
#         result = num1 - num2
#     elif num==3:
#         result = num1 / num2
#     elif num==4:
#         result = num1 * num2
# elif num==5:
#     first = int(input("Enter the first number : "))
#     second = int(input("Enter the second number : "))
#     result = (first+second)/2
# else:
#     result = 0
#     print("number not in range")
# if result<0:
#     print("Negative")
# else:
#     print("result: ", result)


# Question 3: Write a program in Python to implement the given flowchart:
# Answer:
# a, b, c = 10, 20, 30
# avg = (a+b+c)/3
# print("avg= ", avg)

# if (avg > a) and (avg > b) and (avg > c):
#     print(f"Average {avg} is higher than a {a}, b {b}, c {c}")
# elif (avg > a) and (avg > b):
#     print(f"Average {avg} is higher than a {a}, b {b}")
# elif (avg > a) and (avg > c):
#     print(f"Average {avg} is higher than a {a}, c {c}")
# elif (avg > b) and (avg > c):
#     print(f"Average {avg} is higher than b {b}, c {c}")
# elif avg > a:
#     print(f"Average {avg} is just higher than a {a}")
# elif avg > b:
#     print(f"Average {avg} is just higher than b {b}")
# elif avg > c:
#     print(f"Average {avg} is just higher than c {c}")


# Question 4: Write a program in Python to break and continue if the following cases occurs:
# 1. If user enters a negative number just break the loop and print “It’s Over”
# 2. If user enters a positive number just continue in the loop and print “Good Going”
# Answer:
# 








