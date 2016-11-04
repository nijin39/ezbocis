from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from ezbocis.ezbocis_blueprint import ezbocis
import os

@ezbocis.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(ezbocis.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@ezbocis.route("/")
def hello():
	return render_template("home.html")

'''
JSON SAMPLE CODE
'''
@ezbocis.route("/restful")
def restTest():
	dic = {'name' : 'pey', 'phone' : '010990303', 'bitrh' : '1118'}
	return jsonify(results=dic)

@ezbocis.route("/home")
def index():
	return render_template("home.html")

'''
Server Service
'''
@ezbocis.route("/serverList")
def serverList():
	return render_template("serverList.html")

@ezbocis.route("/serverRegistration")
def serverRegistration():
	return render_template("serverRegistration.html")

@ezbocis.route("/test")
def test():
	return render_template("test.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
