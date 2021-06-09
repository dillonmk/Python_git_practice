## This file will be about creating functions in python

import os
os.system('clear')

#### FUNCTIONS ####
# other programs can call them methods

# Insisde parenthasis you pass in arguments

def nameit(name):
    print("Hello " + name)


nameit("Dillon")

# can have multiple input arguments

first_name = "Dillon"
last_name = "Kabot"
def firstLast(first_name, last_name):
    print("The name is " + first_name + " " + last_name)

firstLast(first_name, last_name)

#math functions
def mathit(num1, num2):
    return(num1 + num2)

answer = mathit(3,5)

print(answer)

# RETURN #
#Returns the outcome of the function
# Gives us more control over the functions
# allows assignment or just making of hidden variable
