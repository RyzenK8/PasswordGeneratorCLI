# Dependency and combination characters
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

# The password generator configuration
all = lower + upper + numbers +symbols
length = 32
password = "".join (random. sample (all, length))

# Output CLI
print ('Warning, This project is in alpha or development stage. Maybe may have some malfunctions. Can try to compile the program native working for you systems.')
print (' ')
print ('================================')
print (password)
print ('================================')
