## Talking about Fizz Buzz
## Popular interview question from years ago

# The question goes like this:
# You want to print out all numbers from 1 to 100 on screen
# If the number is divisable by 3, print Fizz
# If the number is divisable by 5, print Buzz
# If the number is divisable by 3 & 5, print FizzBuzz

import os
os.system('clear')

counter = 1

while (counter <=100):
    if (counter%3 == 0 and counter%5 == 0):
        print(str(counter) + " Fizz Buzz")
    elif(counter%3 == 0):
        print(str(counter) + " Fizz")
    elif(counter%5 == 0):
        print(str(counter) + " Buzz")
    else:
        print(str(counter))
    counter += 1
