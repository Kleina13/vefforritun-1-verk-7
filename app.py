# APP

from flask import Flask, render_template as rend, url_for
from pymysql import *

app = Flask(__name__)

conn = connect(host='tsuts.tskoli.is', port=3306, user='2208022210', password='mypassword', database='2208022210_...')
	
@app.route('/')
def index():
	with conn.cursor() as cursor:
		cursor.execute("SELECT * FROM user")    
		album = cursor.fetchall()

	return str(album)



# error <<<<<<<<<<<
@app.errorhandler(400)
def error400(error):
	return rend('error.html', error_type=400, error=error)
@app.errorhandler(401)
def error401(error):
	return rend('error.html', error_type=401, error=error)
@app.errorhandler(403)
def error403(error):
	return rend('error.html', error_type=403, error=error)
@app.errorhandler(404)
def error404(error):
	return rend('error.html', error_type=404, error=error)
@app.errorhandler(500)
def error500(error):
	return rend('error.html', error_type=500, error=error)
@app.errorhandler(502)
def error502(error):
	return rend('error.html', error_type=502, error=error)
@app.errorhandler(503)
def error503(error):
	return rend('error.html', error_type=503, error=error)
@app.errorhandler(504)
def error504(error):
	return rend('error.html', error_type=504, error=error)
# error <<<<<<<<<<<

if __name__ == "__main__":
	app.run(debug=True)
