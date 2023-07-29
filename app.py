import model
from flask import * 
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 

X=''
app = Flask(__name__)  

app.secret_key = 'your secret key'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sharmi@15'
app.config['MYSQL_DB'] = 'account'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
 
 
mysql = MySQL(app)

@app.route('/')  
def upload():  
    return render_template("index.html")

@app.route('/files',methods = ['POST'])   
def file():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM login WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return render_template('file.html')
        else:
           return render_template("index.html")

    #  if request.method == 'POST':
    #     username=request.form['username']
    #     print(username)
    #     if(username=='sharmi'):

    #         print('sharmi')
    #         return render_template("file.html")  
    #     else:
    #         return render_template("index.html")
 
@app.route('/success', methods = ['POST'])  
def success():  
    global X
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)

        X = f.filename
        print(X)
        period=request.form['itemname']
        print(period)
        num=request.form['num']
        print(num)
        model.fuc(f.filename,period,num)
        # model.fuc(f.filename)

# @app.route('/details', methods = ['POST'])  
# def next():
   
#    if request.method=='POST':
#        print(X+'***')
#        period=request.form['itemname']
#        print(period)
#        num=request.form['num']
#        print(num)
#        model.fuc(X,period,num)
  
if __name__ == '__main__':  
    app.run(debug = True)