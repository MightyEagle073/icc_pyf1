# ICC Python Fundamentals 1, Week 2, Exercise 4: zoo_rhyming_couplets.py
# By [your name] on [date]
#
# You're visiting the zoo and feeling inspired by the fascinating animals you 
# encounter! Let's create a program that asks you for the names of two animals 
# and generates a rhyming couplet about them.
# 
# Input: You will provide the names of two animals when prompted by the program.
# Output: The program will print out a rhyming couplet based on the names of the 
# two animals you provided.
#
# Your program MUST NOT use the f-string method! If you do, you will receive
# a 0 for this exercise!

animal1 = input("Enter the name of the first animal: ")
animal2 = input("Enter the name of the second animal: ")

print()
print("Here's a rhyming couplet about the", animal1, "and the", animal2 + ":")
print("The", animal1, "roars with might and brawn,")
print("While the", animal2, "glides gracefully at dawn.")