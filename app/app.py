from flask import Flask, url_for, render_template, request, session
import sqlite3

app = Flask(__name__)
id = ''
name = ''
photo = ''
marks = ''
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('registration.html')

@app.route("/success", methods = ['POST'])
def my_form_post():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
      c.execute('''SELECT * FROM STUDENT''')
      #c.execute('')
      c.execute('''DELETE FROM STUDENT''')
    except:
      c.execute('''CREATE TABLE STUDENT(id text, name text, dob text, photo text, gender text, result text)''')
    conn.commit()
    c.execute('''SELECT COUNT(1) FROM STUDENT''')
    n = c.fetchone()[0]
    name = request.form['name']
    dob = request.form['dob']
    if(request.form['optradio1'] == 'on'):
        gender = "MALE"
    else:
        gender = "FEMALE"
    id = "SAT"
    n += 1
    if(n<10):
      id += "00"
    elif(n<100):
      id += "0"
    id += str(n)
    photo = request.form['photo']
    result = 0
    params = (id,name,dob,photo,gender,result)
    c.execute("INSERT INTO STUDENT VALUES(?,?,?,?,?,?)",params)
    conn.commit()
    conn.close()
    return render_template('registration_success.html', name=name, dob=dob, gender=gender, photo=photo, id = id)

@app.route("/test_enter")
def test_enter():
    return render_template('test_entry.html')

@app.route("/test_wait", methods = ['POST'])
def test_wait():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    global id
    global name
    global photo
    id = request.form['id']
    pwd = request.form['password']
    d = pwd[0:2]+'/'+pwd[2:4]+'/'+pwd[4:]
    params = (id,d,)
    c.execute('SELECT * FROM STUDENT WHERE id = ? AND dob = ?',params)
    row = c.fetchone()
    if row is None:
        return render_template('test_entry.html',error='User ID or Password Invalid!')
    name = row[1]
    photo = row[3]
    conn.close()
    return render_template('test_wait.html',id=id,name=name,photo=photo)

@app.route("/test")
def test():
    '''f = open("static/Q.txt")
    ln=""
    for line in f:
        ln+=line
    arr = ln.split("$$")'''
    global id
    global name
    global photo
    return render_template('test.html',id=id,name=name,photo=photo)

@app.route("/test_after", methods=['POST'])
def test_after():
    #conn = sqlite3.connect('database.db')
    #c = conn.cursor()
    global marks
    id = request.form['id']
    marks = request.form['marks']
    #print(type(m))
    #params = (m,id,)
    #p2 = (id,)
    #c.execute("UPDATE STUDENT SET result = ? WHERE id = ?",params)
    #c.execute('SELECT * FROM STUDENT WHERE id = ?',p2)
    #row = c.fetchone()
    #print(row)
    #row = c.fetchone()
    #conn.commit()
    #conn.close()
    return render_template('test_after.html')

@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/display_result",methods=['POST'])
def display_result():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    id = request.form['id']
    pwd = request.form['password']
    d = pwd[0:2]+'/'+pwd[2:4]+'/'+pwd[4:]
    params = (id,d,)
    try:
      c.execute('SELECT * FROM STUDENT WHERE id = ? AND dob = ?',params)
    except:
      return render_template('result.html',error='User ID or Password Invalid!')
    row = c.fetchone()
    name = row[1]
    dob = row[2]
    photo = row[3]
    gender = row[4]
    #result = row[5]
    #print(result)
    conn.close()
    return render_template('display_result.html',id=id,name=name,dob=dob,photo=photo,gender=gender,result=marks)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000")
  )