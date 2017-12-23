from flask import Flask, render_template, request

app = Flask(__name__)

raspi_id = "127.0.0.1:5000/"


@app.route('/')
def index():
	return "hello world"

@app.route('/profile/<user>')
def profile(user):
	return render_template("profile.html", user=user)

@app.route('/main')
def main():
	return render_template("main.html")

@app.route('/welcome', methods = ['GET', 'POST'])
def welcome():
	card_no = request.values.get("card_no")
	password = request.values.get("password")
	#databaseden card no password check edilecek
	return render_template("payment.html")

@app.route('/help')
def help():
	#led yakma
	return "LED YAK"

@app.route('/payment/<type>')
def payment(type):
	if type == "coin":
		#bozuk para
		pass
	elif type == "paper":
		#nakit para
		pass
	elif type == "credit":
		#kredi karti
		pass
	elif type == "none":
		return render_template("spend.html")
	else:
		return "Wrong page."

@app.route('/spend')
def spend():
	return render_template("spend.html")

@app.route('/spend/<type>')
def spend_type(type):
	if type == "shopnmiles":
		#thynin sitesine
		pass
	elif type == "upgrade":
		#bilet yukseltme
		pass
	elif type == "donate":
		#para bagislama
		pass
	elif type == "more":
		return render_template("payment.html")
	else:
		return "Wrong page."

if __name__ == '__main__':
	app.run()



'''
Python/HTML/CSS Referance Sheet:

@app.route('/')

@app.route('/<username>') #Username is changing
@app.route('<int:number>') #Input is integer
@app.route('/', methods = ['GET', 'POST'])



'''