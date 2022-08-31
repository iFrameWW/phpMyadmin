import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database = 'week7'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE Week7") 

# mycursor.execute("CREATE TABLE TEACHER(ID INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255) ,Department VARCHAR(255),Hiredate DATE,Category VARCHAR(3),Gender VARCHAR(1),Salary INT(7))")

# sql = "INSERT INTO TEACHER (Name,Department, Hiredate, Category, Gender, Salary) VALUES (%s,%s,%s,%s,%s,%s)"
# val =[
#     ('Tanya Nanda','SocialStudies','1994-03-17','TGT','F',25000),
#     ('Saurabh Sharma','Art','1990-02-12','PRT','M',20000),
#     ('Nandita Arora','English','1980-05-16','PGT','F',30000),
#     ('James Jacob','English','1989-10-16','TGT','M',25000),
#     ('Jaspreet Kaur','Hindi','1990-08-01','PRT','F',22000),
#     ('Disha Sehgal','Math','1980-03-17','PRT','F',21000),
#     ('Siddharth Kapoor','Science','1994-09-02','TGT','M',27000),
#     ('Sonali Mukherjee','Math','1980-11-17','TGT','F',24500)
    
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

#---------------------------------------------------------------------------------------------------

# mycursor.execute("CREATE TABLE PROJECTS(ID INT AUTO_INCREMENT PRIMARY KEY,ProjName VARCHAR(255) ,ProjSize VARCHAR(255),StartDate DATE,EndDate DATE,Cost INT(7))")

# sql = "INSERT INTO PROJECTS (ProjName,ProjSize,StartDate,EndDate,Cost) VALUES (%s,%s,%s,%s,%s)"
# val =[
#     ('Payroll-MMS','Medium','2006-03-17','2006-09-16',60000),
#     ('Payroll-ITC','Large','2008-02-12','2008-01-11',500000),
#     ('IDMgmt-LITL','Large','2008-06-13','2009-05-21',300000),
#     ('Recruit-LITL','Medium','2008-03-18','2008-06-01',50000),
#     ('IDMgmt-MTC','Small','2007-01-15','2007-01-29',20000),
#     ('Recruit-ITC','Medium','2007-03-01','2004-06-28',50000),
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

#---------------------------------------------------------------------------------------------------

# mycursor.execute("CREATE TABLE Members(ID INT PRIMARY KEY,Mname VARCHAR(255))")

# sql = "INSERT INTO Members (ID,Mname) VALUES (%s,%s)"
# val =[
#     (1,'Aakash'),
#     (2,'Hirav'),
#     (3,'Vinayak'),
#     (4,'Sheetal'),
#     (5,'Rajeev')
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

#---------------------------------------------------------------------------------------------------

# mycursor.execute("CREATE TABLE RESULT(No INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255), stipend INT(3), Subject VARCHAR(255), Average INT(3) ,Division VARCHAR(20))")

# sql = "INSERT INTO RESULT(name,stipend,subject,average,division) VALUES (%s,%s,%s,%s,%s)"
# val =[
#     ('Sharon',400,'English',38,'THIRD'),
#     ('Amal',680,'mathematics',72,'FIRST'),
#     ('Vedant',500,'Accounts',67,'FIRST'),
#     ('Shakeer',200,'informatics',55,'SECOND'),
#     ('Anandha',400,'History',85,'FIRST'),
#     ('Upasna',550,'Geography',45,'THIRD')
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

#---------------------------------------------------------------------------------------------------

# mycursor.execute("CREATE TABLE SHOPPE(Code INT PRIMARY KEY ,Item VARCHAR(255), company VARCHAR(255), Qty INT(3),City VARCHAR(20),price FLOAT(7,2))")

# sql = "INSERT INTO SHOPPE(Code,Item,company,Qty,City,price) VALUES (%s,%s,%s,%s,%s,%s)"
# val =[
#    (102,'Biscuit','Hide & Seek',100,'Delhi',10.00),
#    (103,'๋Jam','Kissan',110,'Kolkata',25.00),
#    (101,'Coffee','Nestle',200,'Kolkata',55.00),
#    (106,'Sauce','Maggi',56,'Mumbai',55.00),
#    (107,'Cake','Britannia',72,'Delhi',10.00),
#    (104,'Maggi','Nestle',150,'Mumbai',10.00),
#    (105,'Chocolate','Cadbury',170,'Delhi',25.00)
# ]

# mycursor.executemany(sql, val)
# mydb.commit()