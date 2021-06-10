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
# while True:
#     a = int(input("Enter a number: "))
#     if a < 0:
#         print("Its Over")
#         break
#     else:
#         print("Good Going")
#         continue


# Question 5: Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.
# Answer:
# list1 = []
# for i in range(2000,3201):
#     if (i%7 == 0) and (i%5 != 0):
#         list1.append(str(i))
# print(','.join(list1))


# Question 6: What is the output of the following code examples?
# 1. x=123
#    for i in x:
#       print(i)
# Answer: TypeError: 'int' object is not iterable

# 2. i = 0
#    while i < 5:
#       print(i)
#       i += 1
#       if i == 3:
#           break
#       else:
#           print('error')
# Answer: 
# 0
# error
# 1
# error
# 2

# 3. 
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
# Answer:
# 0
# 1
# 2
# 3
# 4


# Question 7: Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
# Answer: 
# for i in range(6):
#     if (i == 3) or (i == 6):
#         continue
#     print(i, end=' ')


# Question 8: Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2
# Answer:
# str1 = input("Enter a string: ")
# c1 = 0
# c2 = 0
# for i in str1:
#     if i.isdigit():
#         c1 += 1
#     elif i.isalpha():
#         c2 += 1
#     else:
#         pass
# print("Letters: ", c2)
# print("Digits: ", c1)


# Question 9: Read the two parts of the question below
# 1. Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# 2. Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)
# Answer: 1.
# num = int(input("Guess the lucky number: "))
# while num != 7:
#     print("The number entered is not the correct number")
#     num = int(input("Guess the lucky number: "))

# 2.
# number = -1
# answer = 'Y'
# while number != 7 and answer != 'N':
#     number = int(input("Guess the lucky number: "))
#     if number != 7:
#         print("The number entered is not the correct number")
#         answer = input("Would you like to continue guessing?(Y/N) ")


# Question 10: Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as:
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.
# Answer:
# counter = 1
# while counter <= 5:
#     print("Type in the", counter, "number")
#     num = int(input("Enter the number: "))
#     if num != 5:
#         print("Try again")
#     else:
#         print("Good Guess!")
#     counter += 1
# else:
#     print("Game over")


# Question 11: In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.
# Answer:
# counter = 1
# while counter <= 5:
#     print("Type in the", counter, "number")
#     num = int(input("Enter the number: "))
#     if num != 5:
#         print("Try again")
#     else:
#         print("Good Guess!")
#         break
#     counter += 1
# else:
#     print("Sorry but that was not very successful")



