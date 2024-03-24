'''
DEV : JAIME C.

SCRIPT DESCRIPTION: CONFIGURE SQLITE3 DATA

'''


 #import engine database pakage

import sqlite3   

 #create database connection (datbase name)

con = sqlite3.connect('market.db')

# creating curosor object by connetion => let us execute sql comands or operations

cur = con.cursor()

#create users table

user_table = '''
             CREATE TABLE IF NOT EXISTS users (
                                 id INTEGER PRIMARY KEY, 
                                 Firtsname TEXT NOT NULL,
                                 Lastname TEXT NOT NULL,
                                 email TEXT UNIQUE NOT NULL,
                                 pasword TEXT NOT NULL)

'''
# EXECUTE SQL (QUERY)

cur.execute(user_table)

#save changes in database

con.commit()


print(" ::: Database market has been created :::")

#close conecction





