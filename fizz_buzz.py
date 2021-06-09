## Talking about Fizz Buzz
## Popular interview question from years ago

# The question goes like this:
# You want to print out all numbers from 1 to 100 on screen
# If the number is divisable by 3, print Fizz
# If the number is divisable by 5, print Buzz
# If the number is divisable by 3 & 5, print FizzBuzz
# Count number of fizzes, buzzes and fizzbuzzes
import os
os.system('clear')

counter = 1
Fizz = 0
Buzz = 0
FizzBuzz = 0

while (counter <=100):
    if (counter%3 == 0 and counter%5 == 0):
        print(str(counter) + " Fizz Buzz")
        FizzBuzz +=1
    elif(counter%3 == 0):
        print(str(counter) + " Fizz")
        Fizz +=1
    elif(counter%5 == 0):
        print(str(counter) + " Buzz")
        Buzz +=1
    else:
        print(str(counter))
    counter += 1

print("Number of Fizz: " + str("{:,}".format(Fizz)))
print("Number of Buzz: " + str("{:,}".format(Buzz)))
print("Number of FizzBuzz: " + str("{:,}".format(FizzBuzz)))
