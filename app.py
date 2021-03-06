from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import url_for
from flask import render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
	return "HEELO WORLD!!!!"

'''
JSON SAMPLE CODE
'''
@app.route("/restful")
def restTest():
	dic = {'name':'pey', 'phone':'010990303', 'bitrh': '1118'}
	return jsonify(results=dic)

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/remote")
def remote():
	return render_template("remote.html")

@app.route('/hello', methods=['POST'])
def saveScript():
    scriptTitle=request.form['scriptTitle']
    scriptContent=request.form['scriptContent']
    print(scriptTitle,scriptContent)
    return render_template('view-script.html', scriptTitle=scriptTitle, scriptContent=scriptContent)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
