# Dependency and combination characters
import random
import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

# The password generator configuration
all = lower + upper + numbers +symbols

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
    if (length > 100):
        print("\nMaximum length is 100 characters.")
        length = None
  
password = "".join (random. sample (all, length))

# Output CLI
print ('Warning, This project is in alpha or development stage. Maybe may have some malfunctions. Can try to compile the program native working for you systems.')
print (' ')
print ('Your password has been generated !')
print ('================================')
print (password)
print ('================================')
print (' ')

input("Press the enter button to exit.")
sys.exit()
