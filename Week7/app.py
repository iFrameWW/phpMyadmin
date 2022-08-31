from traceback import print_tb
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import mysql.connector

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
host = 'localhost'
user = 'root'
password = ''
db = 'week7'

@app.route("/")
def helloWorld():
      return "Hello, cross-origin-world!"

@app.route("/week7/1/1") # /week7/1/1
def No1_1():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT * FROM TEACHER WHERE Category ='PGT' ")
  myresult = mycursor.fetchall()
  return jsonify(myresult)

@app.route("/week7/1/2")
def No1_2():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT Name FROM TEACHER WHERE Gender ='F' AND Department = 'Hindi' ")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult),200)

@app.route("/week7/1/3")
def No1_3():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT Name,department,hiredate FROM TEACHER ORDER BY Hiredate")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult),200)

@app.route("/week7/1/4")
def No1_4():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT DISTINCT category FROM teacher")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult),200)

@app.route("/week7/2/1")
def No2_1():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT * FROM PROJECTS WHERE ProjSize = 'Medium' ORDER BY ProjName")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/2/2")
def No2_2():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT ProjSize FROM PROJECTS WHERE ProjName LIKE '%LITL'")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/2/3")
def No2_3():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT id,ProjName,ProjSize,cost FROM PROJECTS ORDER BY StartDate DESC")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/2/4")
def No2_4():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT DISTINCT ProjSize FROM projects")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/3/1")
def No3_1():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT Mname FROM Members WHERE Mname LIKE '%v'")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/3/2")
def No3_2():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT Mname FROM Members WHERE Mname LIKE '%e%'")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/4/1")
def No4_1():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT Name FROM RESULT WHERE division LIKE 'FIRST' ORDER BY name DESC ")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/5/1")
def No5_1():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT item FROM shoppe WHERE item LIKE 'C%' ORDER BY price ")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/week7/5/2")
def No5_2():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT code,item,city FROM shoppe WHERE qty <100 ")
  myresult = mycursor.fetchall()
  return make_response(jsonify(myresult))

@app.route("/test")
def No1_1t():
  mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT * FROM TEACHER WHERE Category ='PGT' ")
  myresult = mycursor.fetchall()
  table_teacher = []
  c_table = {}
  for res in myresult:
        c_table = {'Id': res['ID'], 'Name': res['Name'], 'Category' : res['Category']}
        table_teacher.append(c_table)
        c_table = {}
  return jsonify(table_teacher)

#{'id': res['ID'], 'name': res['Name'],'department': res['Department'], 'hiredate': res['Hiredate'], 'category' : res['Category'], 'Gender': res['Gender'], 'salary' : res['Salary']}