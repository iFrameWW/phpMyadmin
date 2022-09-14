import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database = 'WEB'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE WEB") 

# mycursor.execute("""CREATE TABLE User_info(
#     ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#     NAME VARCHAR(255) NOT NULL,
#     EMAIL VARCHAR(255),
#     USERNAME VARCHAR(255) NOT NULL,
#     PASSWORD VARCHAR(255),
#     ROLE INT NOT NULL,
#     FOREIGN KEY (ROLE) REFERENCES ROLES(ID))""")


# mycursor.execute("CREATE TABLE ROLES(ID INT PRIMARY KEY NOT NULL,CLASS VARCHAR(255) NOT NULL)")

# sql = "INSERT INTO ROLES(ID,CLASS) VALUES (%s,%s)"
# val = [
#     (1,'USER'),
#     (2,'STAFF'),
#     (3,'ENGINEER'),
#     (5,'ADMIN')
# ]

# mycursor.executemany(sql,val)
# mydb.commit()

# mycursor.execute("ALTER TABLE ROLES ADD rkey VARCHAR(10)")
'''
    Bna5AeuS8N
    FvMf75GOaY
    WKNsvA8qk3
'''
# sql='UPDATE ROLES SET rkey=%s WHERE ID=%s'
# sql = "INSERT INTO ROLES(ID,CLASS,rkey) VALUES (%s,%s,%s)"
# val =[
#     ('NULL',1),
#     ('Bna5AeuS8N',2),
#     ('FvMf75GOaY',3),
#     ('WKNsvA8qk3',5)
#     ]

# mycursor.executemany(sql,val)
# mydb.commit()

sql = "SELECT Customers.CustomerId Customers.Name Orders.orderId Orders.CustomerId Orders.OrderDate From Customers LEFT OUTER JOIN Orders ON Customers.CustomerId=Orders.CustomerId"