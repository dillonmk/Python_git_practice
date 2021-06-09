## For loops in python

import os
os.system('clear')


name = "Dillon"

# x is just placeholder variable
# convention is to have a 'singular item' where x is
# could do 'banana in name'
for x in name:
    print(x)

#dictionaries as well
favorite_pizza = {
    "Dillon" : "Supreme Pizza",
    "John" : "Pepperoni",
    "Tim" : "Cheese",
}

for key,value in favorite_pizza.items():
    print(key)
    print(value)
