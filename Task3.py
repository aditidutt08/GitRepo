# Question 1: Create a list of 10 elements of four different data types like int, string, complex and float.
# Answer:
# list1 = [2,4.5,"hello",8,1+2j,1.2,"everyone",7+9j,3.2,"good"]


# Question 2: Create a list of size 5 and execute the slicing structure
# Answer: executing slicing
# list1 = [2,6,8,4,6]
# a = list1[:5]
# print(a)   ---> Output: [2,6,8,4,6]

# Another example:
# list1 = [2,6,8,4,6]
# a = list1[2]
# print(a)   ----> Output: 8


# Question 3: Write a program to get the sum and multiply of all the items in a given list.
# Answer: 
# def list_multiply(list1):
#     result = 1
#     for i in list1:
#         result *= i
#     return result


# def list_addition(list1):
#     result = 0
#     for i in list1:
#         result += i
#     return result

# print(list_multiply([2,3,6,4]))
# print(list_addition([4,6,8,2]))


# Question 4: Find the largest and smallest number from a given list.
# Answer: 
# list1 = [2,5,7,10,23,0,19]
# print("Minimum number in the list: ",min(list1))
# print("Maximum number in the list: ",max(list1))
# Output: 
# Minimum number in the list:  0
# Maximum number in the list:  23


# Question 5: Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.
# Answer: 
# list1 = [2,5,7,10,23,0,19]
# for i in list1:
#     if (i%2 == 0):
#         list1.remove(i)
# print(list1)
# Output: [5, 7, 23, 19]


# Question 6: Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).
# Answer: 
# list1 = []
# for i in range(1,31):
#     list1.append(i**2)
# print(list1[:5])
# print(list1[-5:])
# Output: 
# [1, 4, 9, 16, 25]
# [676, 729, 784, 841, 900]


# Question 7: Write a program to replace the last element in a list with another list.
# Answer:
# list1 = [1,3,5,7,9,10]
# list2 = [2,4,6,8]
# list1[-1:] = list2
# print(list1)


# Question 8: Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
# Answer: 
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {}
# for i in [a,b]:
#     c.update(i)
# print(c)
# Output: {1: 10, 2: 20, 3: 30, 4: 40}


# Question 9: Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Answer:
# n = int(input("Enter the value of n: "))
# dict1 = {}
# for i in range(1,n+1):
#     dict1[i] = i*i
# print(dict1)
# Output: 
# Enter the value of n: 5
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Question 10: Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Answer:
# numbers = input("Enter the numbers with comma separated: ")
# list1 = numbers.split(",")
# tuple1 = tuple(list1)
# print("List of numbers: ", list1)
# print("Tuple of numbers: ", tuple1)
# Output : 
# Enter the numbers with comma separated: 34,67,55,33,12,98
# List of numbers:  ['34', '67', '55', '33', '12', '98']
# Tuple of numbers:  ('34', '67', '55', '33', '12', '98')
