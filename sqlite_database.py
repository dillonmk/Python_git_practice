## This file will be the practice file for sqlite


##### SQLite Database #####

import os
os.system('clear')

## SQLite is good for small to medium databases
## This is a preinstalled module

import sqlite3

# Connect to the database in the background

# conn is just a variable
conn = sqlite3.connect('customer.db')
# If database doesnt exist, python will just create it

#create cursor: use cursor to make query, or do stuff with database
c = conn.cursor()


#create a table
# Inside the triple quotes is sqlite 'language' not python
# Take intro to sqlite course
# Column and then data type
#5 types: text, int, real (decimals), blob (images, wavs, mp3, etc.), null or not null
'''
c.execute("""CREATE TABLE customer (
            first_name text,
            last_name text,
            email text
            )""")
'''

# Inserting data into TABLE
#c.execute("INSERT INTO customer VALUES ('John','Elder','john@codemy.com')")
#If wanted print confirm
# print("Data added to table")

# Now we need to maybe pull data out of the TABLE
# * means select everything
c.execute("SELECT * FROM customer")
# can fetch one or many items from returned tuple
print(c.fetchall())

items = c.fetchall()
for item in items:
    print(item)


#commit our changes
conn.commit()



# Close database connection
conn.close()
