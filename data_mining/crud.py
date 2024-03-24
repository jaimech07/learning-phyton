'''
C =>Create (INSERT INTO)
K => Read (SELECT)
U => Update (UPDATE)
D => Delete(DELETE)


'''

from database import con, cur , sqlite3

#create a new user

new_user = '''
       INSERT INTO 
       users (id, Firtsname,Lastname,email,pasword)
       values('23', 'jaime' ,'chilama' , 'jchilama@gmail.com', '1234')    '''
con.execute(new_user)
con.commit()

print("::: New user  has been created sucessfully:::")
#close conection
con.close()
