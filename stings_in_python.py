### File to discuss strings

import os
os.system('clear')

#single or double quotations doesnt matter except for specific
#circumstances such as displaying quotes in printed string
greetings = 'My boss yelled "Get to work!"\n'
print(greetings)

#Some Escape charachters in python:
# \ (backslash) ignore next charachter
# \n new line
#
dog_names = "What is your \n dogs \"name\"? \n"
print(dog_names)


#Concatination can only be done with strings
introduction = "Hello, my name is"
name = "Dillon"

print(introduction + " " + name)


#functions that can be run on strings
#.upper()
#.lower()
#.capitalize()
#.title()
#.swapcase()
#

print(greetings.upper())

#logic type things can be run on strings
print("length of greetings is " + str(len(greetings)))
print("The 15th charachter in greetings is " + greetings[15])

#Ranges can be returned from strings, so
print(introduction[0:5])

#Strings can be split
print(" ")
#So for the following example, introduction is split into a
#list, everywhere that there is a " " (space)
#if a list item is added to the end, it will only print that
#specific item. soooo
# ranges can be run as well
print(introduction.split(" "))
print(introduction.split(" ")[2])
