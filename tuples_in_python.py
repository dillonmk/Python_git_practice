##File to discuss and practice tuples

import os
os.system('clear')

#Tuples are immutable
#Tuples are supposedly a tiny bit faster than lists

tuple1 = ("john", "bob","tina")
tuple2 = ("mary",)
#hacky way to change tuples
#not really changing tuples, just making new tuples with
#    various parts of other tuples
tuple3 = tuple1 + tuple2


print(tuple1)
print(tuple3)

print(tuple1[0:2])

tuple4 = tuple1[0:2] + tuple2
print(tuple4)
