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

