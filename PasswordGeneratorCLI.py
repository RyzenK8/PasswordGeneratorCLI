# Dependencies
import random
import sys

# Intro
print("\033[1;33m\n")
print("The project was created, By RyzenK8 ^^")
print()
print("PasswordGeneratorCLI")
print()

# The password generator configuration
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

# Configuration make password.
all = lower + upper + numbers + symbols

# Set the password length to None to start the loop
# This is so that the program will keep asking for a length until a valid one is entered
length = None
while (length == None): 
    # Try to convert the input to an integer
    try:
        length = int(input("Enter desired password length: "))
    # If the input is not an integer, set the length to None
    except ValueError:
        print("\nInvalid length. Please enter a numerical value.")
        length = None
    # Set a limit so that the program doesn't crash
    if (length > 75):
        print("\nMaximum length is 75 characters.")
        length = None

# Double the characters in the string if the length is greater than the number of characters
while (length > len(all)):
    all = all + all
  
password = "".join(random.sample(all, length))

# Output CLI
print("\033[1;32m\n")
print ('Thank you for using our PasswordGeneratorCLI.')
print ()
print ('Your password has been generated !')
print ()
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print (password)
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ()

# System exit
input("Press the enter button to exit.")
sys.exit()
