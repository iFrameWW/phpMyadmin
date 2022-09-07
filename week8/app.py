from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
import pymysql
 
app = Flask(__name__)
  
mysql = MySQL()
   
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'week7'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route('/')
def Index():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
 
    cur.execute('SELECT * FROM shoppe')
    data = cur.fetchall()
  
    cur.close()
    return render_template('index.html', datab = data)

@app.route('/test')
def Test():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
 
    cur.execute('SELECT * FROM shoppe')
    data = cur.fetchall()
  
    cur.close()
    return render_template('text.html', datab = data)

@app.route('/add_supply', methods=['POST'])
def add_employee():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        Item = request.form['item']
        company = request.form['company']
        Qty = request.form['qty']
        City = request.form['city']
        price = request.form['price']

        cur.execute("INSERT INTO shoppe (Item, company, Qty, City, price) VALUES (%s,%s,%s,%s,%s)", (Item, company, Qty, City, price))
        conn.commit()
        flash('Suply Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', datab = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_employee(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE employee
            SET name = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Employee Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<id>', methods = ['POST','GET'])
def delete_employee(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('DELETE FROM employee WHERE id = {0}'.format(id))
    conn.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('Index.html'))
 
# starting the app
if __name__ == "__main__":
    app.run()
