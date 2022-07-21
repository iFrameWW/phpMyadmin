import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database ="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE restaurant (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), location VARCHAR(255), phone_number VARCHAR(255))")

# mycursor.execute("CREATE TABLE food_product (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255), quantity VARCHAR(255))")

# mycursor.execute("CREATE TABLE cart (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255), quantity VARCHAR(255))")

# mycursor.execute("CREATE TABLE customers (ID INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), phone_number VARCHAR(255), home_number VARCHAR(255), road_name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE TABLE payment (Credit_card_band VARCHAR(255), Credit_card_number VARCHAR(255), Credit_card_holder VARCHAR(255))")

# sql = "INSERT INTO customers (first_name, last_name, phone_number, home_number, road_name, address) VALUES (%s, %s, %s, %s, %s, %s)"
# val = [
#     ('Wonsgathorn','Wanwong','0972355339','103/5','sukumvit','moo.5'),
#     ('Kornkanok','Pobchan-ad','0973504742','111/1','highway 21','-'),
#     ('David','Jhon','0978521478','121/7','highway 23','-'),
#     ('Bau','ponlawat','0987521589','169','rong-had road','-'),
#     ('Jhon','GATEWOOD','0999999999','169','rong-had road','-'),
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record was inserted.")

# sql = "INSERT INTO restaurant (name, location, phone_number) VALUES (%s, %s, %s)"
# val = [
#     ('KFC','Lamthong Bangsaen','-')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record was inserted.")

