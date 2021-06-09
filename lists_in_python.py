#This file is going to be the learning File
# to discuss lists in python

import os
os.system("clear")

names = ["Dillon", "bob", "john"]
#we can change a specific list item with
names[1] = 'Terry'
print(names[0])
print(names[1])

#add item to end of lists
names.append("wes")
print(names)

#lists inside of lists
nums = [1,2,3,4,5]

names.append(nums)
print(names)

#access list item from list inside of a list
#do math on called list item
print(names[4][2]*3)
print(len(names))

#finding the last item in a list
print(names[len(names)-1])


#Dictionary can be inside a lists
