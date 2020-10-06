from flask import Flask,jsonify,request,url_for,redirect,session,render_template
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisissecret!'

def connect_db():
	sql = sqlite3.connect('/C:/Program Files/sqlite3/sqlite3/data.db')
	sql.row_factory = sqlite3.Row
    return sql
def get_db():
	if not hasattr(g,'sqlite3'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
    	g.sqlite_db.close()

@app.route('/')
def index():
	session.pop('name',None)
	return '<h1>HELLO WORLD!</h1>'

@app.route('/home',methods=['POST','GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST','GET'])
def home(name):
	session['name'] = name
	return render_template('home.html',name=name,display=False,mylist = ['one','two','three','four'])

@app.route('/json')
def json():
	if 'name' in session:
	    name = session['name']
	else:
		name = 'NotInSession'
	return jsonify({'key' : 'value', 'listkey' : [1,2,3],'name':name})

@app.route('/theform',methods = ['GET','POST'])
def theform():
	if request.method == 'GET':
	    return render_template('form.html')

	else:
		name = request.form['name']
		return redirect(url_for('home',name=name))

if __name__ == '__main__':
	app.run()