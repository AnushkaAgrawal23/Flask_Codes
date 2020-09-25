from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>HELLO WORLD!</h1>'

@app.route('/home/<name>', methods=['GET'])
def home(name):
	return '<h1>You {} are on the home page!</h1>'.format(name)

@app.route('/json')
def json():
	return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

if __name__=='__main__':
	app.run(debug=True)