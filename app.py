from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("home.html")

'''
JSON SAMPLE CODE
'''
@app.route("/restful")
def restTest():
	dic = {'name' : 'pey', 'phone' : '010990303', 'bitrh' : '1118'}
	return jsonify(results=dic)

@app.route("/home")
def index():
	return render_template("home.html")

'''
Server Service
'''
@app.route("/serverList")
def serverList():
	return render_template("serverList.html")

@app.route("/serverRegistration")
def serverRegistration():
	return render_template("serverRegistration.html")

'''
Script Service
'''
@app.route("/scriptList")
def scriptList():
	return render_template("scriptList.html")
	
@app.route("/scriptRegistration")
def scriptRegistration():
	return render_template("scriptRegistration.html")
	
@app.route("/test")
def test():
	return render_template("test.html")

@app.route("/script")
def remote():
	return render_template("script.html")

@app.route('/hello', methods=['POST'])
def saveScript():
    scriptTitle=request.form['scriptTitle']
    scriptContent=request.form['scriptContent']
    print(scriptTitle,scriptContent)
    return render_template('view-script.html', scriptTitle=scriptTitle, scriptContent=scriptContent)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
