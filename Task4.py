# Question 1: Write a program to reverse a string.
# Answer:
# def reverse_string(string1):
#     new_str = ""
#     for i in string1:
#         new_str = i + new_str
#     return new_str


# string1 = "1234abcd"
# print(reverse_string(string1))
# Output: dcba4321


# Question 2: Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Answer: 
# def calculate_string(string1):
#     upper_case, lower_case = 0, 0
#     for i in string1:
#         upper_case += i.isupper()
#         lower_case += i.islower()
#     return "No. of Uppercase characters: ",upper_case, "No. of Lowercase characters: ", lower_case

# string1 = "abcSdefPghijQkl"
# print(calculate_string(string1))
# Output: ('No. of Uppercase characters: ', 3, 'No. of Lowercase characters: ', 12)


# Question 3: Create a function that takes a list and returns a new list with unique elements of the first list.
# Answer: 
# def unique_vals_list(list1):
#     new_list = []
#     for i in list1:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# list1 = [2,4,2,7,3,5,4,9,2,9,4,6,0]
# print("Unique values in a list: ", unique_vals_list(list1))
# Output: Unique values in a list:  [2, 4, 7, 3, 5, 9, 6, 0]


# Question 4: Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
# Answer:
# str_input = input("Enter the hyphen separated string: ")
# new_str = str_input.split("-")
# new_str.sort()
# print("-".join(new_str))
# Output: Enter the hyphen separated string: H-E-L-L-O-E-V-E-R-Y-O-N-E
# E-E-E-E-H-L-L-N-O-O-R-V-Y


# Question 5: Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Answer: 
# lines = []
# while True:
#     new_lines = input()
#     if new_lines:
#         lines.append(new_lines.upper())
#     else:
#         break
# for i in lines:
#     print(i)
# Output: Hello world Practice makes man perfect
# HELLO WORLD PRACTICE MAKES MAN PERFECT


# Question 6: Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
# Answer: 
# def calculate_sum(num1,num2):
#     sum = int(num1) + int(num2)
#     return sum

# print(calculate_sum("4","3"))
# Output: 7


# Question 7: Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
# Answer: 
# def string_length(str1, str2):
#     if (len(str1) == len(str2)):
#         print(str1)
#         print(str2)

#     elif (len(str1) < len(str2)):
#         print(str2)

#     else:
#         print(str1)


# str1 = input("Enter the First String: ")
# str2 = input("Enter the Second String: ")

# print("\n")

# string_length(str1, str2)
# Output: Enter the First String: hello hi this is me
# Enter the Second String: hello hi this is me
# hello hi this is me
# hello hi this is me


# Question 8: Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
# Answer:
# def generateTuple():
#     new_list = []
#     for i in range(1,21):
#         new_list.append(i**2)
#         new_tuple = tuple(new_list)
#     print(new_tuple)

# generateTuple()
# Output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)


# Question 9: Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Answer:
# def showNumbers(limit):
#     for i in range(limit+1):
#         if i%2 == 0:
#             print(i, end=" ")
#             print("EVEN")
#         else:
#             print(i, end=" ")
#             print("ODD")


# print(showNumbers(3))
# Output: 
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


# Question 10: Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
# Answer:
# list1 = range(1,21)
# even_nums = lambda x: x%2 == 0
# list2 = list(filter(even_nums, list1))
# print(list2)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Question 11: Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Answer: 
# list1 = [1,2,3,4,5,6,7,8,9,10]
# square_nums = lambda x: x**2
# even_nums = lambda x: x%2 == 0
# list2 = map(square_nums, filter(even_nums, list1))

# print(list(list2))
# Output: [4, 16, 36, 64, 100]


# Question 12: Write a function to compute 5/0 and use try/except to catch the exceptions
# Answer:
# def division():
#     return 5/0

# try:
#     division()
# except ZeroDivisionError:
#     print("Division by zero")
# except Exception as e:
#     print("Some other exception")
# finally:
#     print("In the finally block")
# Output:
# Division by zero
# In the finally block


# Question 13: Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
# Answer: 
# from functools import reduce

# list1 = [1,2,3,4,5,6,7]
# list_join = reduce(lambda a,b: 10*a+b, list1, 0)

# print(list_join)
# Output: 1234567


# Question 14: Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.


