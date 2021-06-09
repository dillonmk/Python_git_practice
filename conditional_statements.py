### conditional statements

import os
os.system("clear")

# if / else /elif

num = 6

#tabs are necessary
if (num > 10) :
    print(str(num) + " is greater than 10")
elif (num == 10):
    print(str(num) + " is equal to 10")
else:
    print(str(num) + " is less than 10")


#conditionals can be nested

#multiple conditionals
# and or 

num = 101

#tabs are necessary
if (num > 10) and (num>100) :
    print(str(num) + " is greater than 10")
