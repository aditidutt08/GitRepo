# Question 1: Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
# Answer: 
# a, b, c = 10, 1.80, 'Hello'


# Question 2: Create a variable of type complex and swap it with another variable of type integer.
# Answer: 
# a = complex(1,2)
# b = 10
# a, b = b, a
# print("a= ", a)
# print("b= ", b)
# Output: a = 10
#         b = 1+2j    


# Question 3: Swap two numbers using a third variable and do the same task without using any third variable.
# Answer: 
# a = complex(1,2)
# b = 10
# temp = a
# a = b
# b = temp
# print("a= ", a)
# print("b= ", b)
# Output: a = 10
#         b = 1+2j


# Question 4: Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.
# Answer: 
# a = input("Enter the value of a: ")
# printing in python 3.x
# print("The value of a is: ", a)
# printing in python 2.x
# print "The value of a is: " + a


# Question 5: Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.
# Answer: 
# taking input from the user
# a = int(input("Enter the value of a between 1 to 10: "))
# b = int(input("Enter the value of b between 1 to 10: "))
# if (a > 0 and a <= 10) and (b > 0 and b <= 10):
#     z = a + b
#     z += 30
#     result = z
#     print(result)
# else:
#     print("Entered values not in range")
# Output: 
# Enter the value of a between 1 to 10: 3
# Enter the value of b between 1 to 10: 6
# 39


# Question 6: Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc
# Answer: 
# a = input("Enter the value of a: ")
# print("The data type of the input value is : ", type(a))
# Output: 
# Enter the value of a: hello
# The data type of the input value is : <class 'str'>


# Question 7: Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
# Answer: 
# upper camelcase
# first_var = 'HiHello'
# lower camelcase
# second_var = 'hiHello'
# SnakeCase
# third_var = 'hi_hello'
# uppercase
# fourth_var = 'HIHELLO'


# Question 8: If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?
# Answer:
# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again, the value of ‘a’ will change to the latest value assigned to it. For example, if we write the following code:
# a = 6
# a = "hi"
# print(a)
# The output would be the latest value assigned to ‘a’ which is “hi”.


    
