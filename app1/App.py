# mi primer app en python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL  

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dikeroil'
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur= mysql.connection.cursor()
    cur.execute('select id, fullname, phone, email from contacts')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        cur = mysql.connection.cursor()
        cur.execute('insert into contacts (fullname,phone,email) values (%s,%s,%s)', (fullname,phone,email))
        mysql.connection.commit()
        flash('CONTACTO AGREGADO')             
        return redirect(url_for('Index'))

@app.route('/edit_contact/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, fullname, phone, email FROM contacts where id ={0}'. format(id))
    data = cur.fetchall()
    print(data)
    return render_template('edit-contact.html', contacts = data)

@app.route('/delete_contact/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from contacts where id ={0}'. format(id))
    mysql.connection.commit()
    flash('CONTACTO BORRADO')
    return redirect(url_for('Index'))
    
@app.route('/update_contact/', methods=['POST'])
def update_contact():
    if request.method == 'POST':        
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        idx = request.form['id']        
        cur = mysql.connection.cursor()
        cur.execute("""
            update contacts 
            set fullname=%s,
                phone=%s,
                email=%s 
            where id =%s
        """, (fullname,phone,email,idx))
        mysql.connection.commit()
        flash('CONTACTO EDITADO')             
    return redirect(url_for('Index'))




if __name__ == '__main__':
    app.run(port=3000, debug=True)