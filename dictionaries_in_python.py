#This file will be about Dictionaries and
#practicing some of their various things
# Can use numbers, arrays and other items in Dictionaries

import os
os.system('clear')

#key and value pair (can be on one line)
favorite_pizza = {
    "Dillon" : "Supreme Pizza",
    "John" : "Pepperoni",
    "Tim" : "Cheese",
}

print(favorite_pizza)

#pass in key
print(favorite_pizza["Dillon"])

#deleting an item
del favorite_pizza["Tim"]
print(favorite_pizza)

#adding an item to end
favorite_pizza.update({"Tina":"Sausage"})

print(favorite_pizza)

#updating an item in the Dictionary
favorite_pizza["John"] = "Green Peppers"
print(favorite_pizza['John'])
