from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'software_engineering'

@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		return '2016112258 이용희<br>Logged in as ' + username + '<br>' + \
			"<b><a href = '/logout'>click here to log out </a></b>"
	return "2016112258 이용희<br>You are not logged in <br><a href = '/login'></b>" + \
		"click here to log in </b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
	2016112258 이용희<br>
	<form action = "" method = "post">
		<p><input type = text name = username></p>
		<p><input type = submit value = Login></p>
	</form>
	'''

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug = True)