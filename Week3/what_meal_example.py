# ICC Python Fundamentals 1, Week 3, Exercise 2: dinnertime.py
# By Oscar Liang on 29/10/2024
#
# It's dinnertime! You haven't had anything to eat all day, and are feeling 
# quite hungry (and thirsty). You head to a secret little restaurant on a 
# bustling little shopping centre, and you see 5 items on the menu: a ch
#
# Input: You will give two numbers for the program to add up.
# 
# Output: The program will print the sum of those two numbers.
#
# If one of your inputs is not a number, then the program should treat it as if
# it is a 0. Failure to do this will result in a 20% deduction of marks.

# Lets user input the first the two numbers
num1 = input("Please input your first number to add: ")
num2 = input("Please input your second number to add: ")

# Convert the first number to an integer if it is numerical, otherwise make it 0
if num1.isnumeric():
    num1 = int(num1)
else:
    num1 = 0

# Convert the second number to an integer if it is numerical, otherwise make it 0
if num2.isnumeric():
    num2 = int(num2)
else:
    num2 = 0

# Print final result
print(f"Your sum is {num1 + num2}.")