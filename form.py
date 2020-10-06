from flask import Flask,jsonify , request

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>HELLO WORLD!</h1>'

@app.route('/home',methods=['POST','GET'], defaults={'name' : 'Default'})
@app.route('/home/<int:name>', methods=['POST','GET'])
def home(name):
	return '<h1>You {} are on the home page!</h1>'.format(name)

@app.route('/json')
def json():
	return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

@app.route('/theform')
def theform():
	return '''<form method = "POST" action = "/process">
	              <input type = "text" name = "name">
	              <input type = "text" name = "location">
	              <input type = "submit" value = "Submit">
	           </form>'''

@app.route('/process',methods = ['POST'])
def process():
	name = request.form['name']
	location = request.form['location']

	return 'Hello {}. You are from {}. You have submitted the form successfully!'.format(name,location)

if __name__ == '__main__':
	app.run(debug=True)