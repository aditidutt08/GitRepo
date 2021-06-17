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
