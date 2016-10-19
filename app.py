from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask import session
import json
import requests
import os
import random
from httplib import responses
import time
import binascii
import sys

sys.path.append("../SHSM")
import aes

app = Flask(__name__)
app.secret_key = "super secret key"
app.config.from_pyfile('config.properties')

@app.route("/")
def index():
    return home()

@app.route("/home")
def home():
	if verify():
	    return render_template("home.html")
	else:
		return login()
	
@app.route("/collect")
def collect():
	if verify():
		return render_template("collect.html")
	else:
		return login() 
        
@app.route("/shsm")
def shsm():
    if verify():
        return render_template("shsm.html")
    else:
        return login() 
    
@app.route("/mkeygen", methods=['POST'])
def masterkeygen():
    if verify():
        payload = {}
        url = app.config['MASTER_KEY_GEN_URL']

        headers = {
        'content-type': "application/json",
        'authorization': "Bearer "+session['accessToken'],
        'cache-control': "no-cache",
        }
        

        response = requests.request("POST", url, headers=headers, verify=False)
        print(response.text)
        return response.text
    else:
        return login()

@app.route("/keygen")
def keygen():
    return aes.make_key()

@app.route("/message/encrypt", methods=['POST'])
def encryptMessage():
    content = request.json
    print content['key']
    print content['message']
    return aes.encrypt_message(content['key'], content['message'])

@app.route("/message/decrypt", methods=['POST'])
def decryptMessage():
    content = request.json
    print content['key']
    print content['message']
    return aes.decrypt_message(content['key'], content['message'])

@app.route("/key/encrypt", methods=['POST'])
def encryptKey():
    content = request.json
    if verify():
        payload = {}
        url = app.config['AES_URL']
        payload['type'] = content['type']
        payload['data'] = content['data']

        headers = {
        'content-type': "application/json",
        'authorization': "Bearer "+session['accessToken'],
        'cache-control': "no-cache",
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
        return response.text
    else:
        return login()

@app.route("/key/decrypt", methods=['POST'])
def decryptKey():
    content = request.json
    if verify():
        payload = {}
        url = app.config['AES_URL']
        payload['type'] = content['type']
        payload['data'] = content['data']

        headers = {
        'content-type': "application/json",
        'authorization': "Bearer "+session['accessToken'],
        'cache-control': "no-cache",
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
        return response.text
    else:
        return login()
    
@app.route("/sendMacAddress", methods=['GET'])	
def sendMacAddress():
	if verify():
		payload = {}
		url = app.config['MAC_URL']
		payload['timestamp'] = time.time()
		payload['mac'] = MACprettyprint(randomMAC())

		headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer "+session['accessToken'],
	    'cache-control': "no-cache",
	    }
        

		response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
		return response.text
	else:
		return login()

@app.route("/macs", methods=['GET'])
def macList():
    if verify():
        url = app.config['MACLIST_URL']

        headers = {
        'content-type': "application/json",
        'authorization': "Bearer "+session['accessToken'],
        'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers, verify=False)
        print('{"data":'+response.text+"}")
        return '{"data":'+response.text+"}"
    else:
        return login()

@app.route("/login", methods=['GET'])
def login():
	if verify():
		return index()
	else:
		return render_template('login.html')
       

@app.route("/logout")
def logout():
	session.clear()
	return login()

@app.route('/login', methods=['POST'])
def do_admin_login():
    if ( authrity(request.form['username'],request.form['password']) ):
        session['logged_in'] = True
        for value in session:
        	print(value, session[value])
    else:
        return login()
    return index()
   
def verify():
	if not session.get('logged_in'):
		return False
	else:
		return True
	
def authrity(username, password):
	url = app.config['APIGW_URL']+"/token"
	payload = "grant_type=password&username=" +username+ "&password=" +password
	headers = {
    'authorization': "Basic " + app.config['CONSUMER'],
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }
	response = requests.request("POST", url, data=payload, headers=headers, verify=False)
	tokenResponse = json.loads(response.text)
	try:	
		
		accessToken = tokenResponse['access_token']
		expiresIn = tokenResponse['expires_in']
		session['accessToken'] = accessToken
		
		if accessToken and expiresIn > 10:
		    return True
		else:
		    return False
	except:
		return False

def randomMAC():
    return [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))


    
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
