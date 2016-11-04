from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from ezbocis.ezbocis_blueprint import ezbocis
import requests
import os

'''
Script Service
'''
@ezbocis.route("/scriptList")
def scriptList():
    return render_template("scriptList.html")
	
@ezbocis.route("/scriptRegistration")
def scriptRegistration():
    return render_template("scriptRegistration.html")
	
@ezbocis.route("/script")
def remote():
    return render_template("script.html")

@ezbocis.route("/job/networkinfo",methods=['POST'])
def job_execute_netowrk():
    url = "http://www.ezbocis.com:5001/job"

    payload = "{\n\t\"id\":\"0001\",\n\t\"script\":\"ifconfig\",\n\t\"type\":\"bat\"\n}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@ezbocis.route("/job/diskinfo",methods=['POST'])
def job_execute_disk():
    url = "http://www.ezbocis.com:5001/job"

    payload = "{\n\t\"id\":\"0001\",\n\t\"script\":\"df -k\",\n\t\"type\":\"bat\"\n}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@ezbocis.route('/hello', methods=['POST'])
def saveScript():
    scriptTitle=request.form['scriptTitle']
    scriptContent=request.form['scriptContent']
    print(scriptTitle,scriptContent)
    return render_template('view-script.html', scriptTitle=scriptTitle, scriptContent=scriptContent)
