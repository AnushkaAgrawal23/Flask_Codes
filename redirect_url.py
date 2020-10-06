from flask import Flask,jsonify,request,url_for,redirect,session
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisissecret!'

@app.route('/')
def index():
	session.pop('name',None)
	return '<h1>HELLO WORLD!</h1>'

@app.route('/home',methods=['POST','GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST','GET'])
def home(name):
	session['name'] = name
	return '<h1>You {} are on the home page!</h1>'.format(name)

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
	    return '''<form method = "POST" action = "/theform">
	                 <input type = "text" name = "name">
	                 <input type = "text" name = "location">
	                 <input type = "submit" value = "Submit">
	               </form>'''

	else:
		name = request.form['name']
		return redirect(url_for('home',name=name))

if __name__ == '__main__':
	app.run()