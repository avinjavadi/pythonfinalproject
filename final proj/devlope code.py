import sqlite3

cnt=sqlite3.connect("shop.db")

#---------------create table---------------

# sql=''' CREATE TABLE products(
#     id INTEGER PRIMARY KEY,
#     pname CHAR(15) NOT NULL,
#     price INTEGER NOT NULL,
#     qnt INTEGER) '''

# cnt.execute(sql)
# print ("products table has been created")

#---------------insert product into table---------------

# sql=''' INSERT INTO products(pname,price,qnt)
#         VALUES("book",2,8000) '''

# cnt.execute(sql)
# cnt.commit()
# print ("data inserted !")

#---------------create table---------------

# sql=''' CREATE TABLE cart(
#     id INTEGER PRIMARY KEY,
#     pid INTEGER NOT NULL,
#     uid INTEGER NOT NULL,
#     qnt INTEGER NOT NULL) '''

# cnt.execute(sql)
# print ("cart table has been created")

#---------------insert data into table---------------

# sql=''' INSERT INTO cart(pid,uid,qnt)
#         VALUES() '''

# cnt.execute(sql)
# cnt.commit()
# print ("data inserted !")

#---------------create table---------------

# sql=''' CREATE TABLE access(
#     uid INTEGER PRIMARY KEY,
#     acc INTEGER NOT NULL) '''

# cnt.execute(sql)
# print ("access level table has been created")