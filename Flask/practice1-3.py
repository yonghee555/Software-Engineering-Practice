from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_ice2(name):
	return '2016112258 이용희<br/>Hello ICE student %s!' %name

if __name__ == "__main__":
	app.run(debug=True)