import sqlite3

cnt=sqlite3.connect("shop.db")

#---------------create users table---------------

# sql=''' CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     user CHAR(15) NOT NULL,
#     pass CHAR(25) NOT NULL,
#     addr CHAR(50),
#     score INTEGER) '''

# cnt.execute(sql)
# print ("table has been created")

#---------------insert data into table---------------

# sql=''' INSERT INTO users(user,pass,addr,score)
#         VALUES("hossein","368739","rasht",20) '''

# cnt.execute(sql)
# cnt.commit()

# user1=input ("username : ")
# pass1=input ("password : ")
# addr1=input ("address : ")
# score1=int (input ("score : "))

# sql=''' INSERT INTO users(user,pass,addr,score)
#         VALUES(?,?,?,?) '''

# cnt.execute(sql,(user1,pass1,addr1,score1))
# cnt.commit()

#---------------fetch data from table---------------

# sql=''' SELECT user,pass,addr FROM users '''
# sql=''' SELECT * FROM users WHERE (addr="rasht") and (score>18 ) '''

# result=cnt.execute(sql)
# rows=result.fetchall()
# print (rows)
# for item in rows :
#         print (item)



#1
# city=input ("city name : ")
# sql=''' SELECT user,pass FROM users WHERE (addr=?) '''
# result=cnt.execute(sql,(city,))
# rows=result.fetchall()
# print (rows)



#2
# user=input ("please enter a username : ")
# pas=input ("please enter a password : ")
# sql=''' SELECT * FROM users WHERE (user=?) and (pass=?) '''
# result=cnt.execute(sql,(user,pas))
# rows=result.fetchall()
# print (rows)

#---------------update table---------------

# sql=''' UPDATE users SET score=19 WHERE user="rezvaneh" '''

# cnt.execute(sql)
# cnt.commit()

#---------------delete record from table---------------

# sql=''' DELETE FROM users WHERE score=19 '''

# cnt.execute(sql)
# cnt.commit()

#---------------sub str---------------

# sql=''' SELECT * FROM users WHERE user like "%ss%" '''

# result=cnt.execute(sql)
# rows=result.fetchall()
# print (rows)



#3
# string=input ("please enter a string : ")
# string="%"+string+"%"

# sql=''' SELECT * FROM users WHERE user like ? '''

# result=cnt.execute(sql,(string,))
# rows=result.fetchall()
# print (rows)