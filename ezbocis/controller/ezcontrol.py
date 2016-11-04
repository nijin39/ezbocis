from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from ezbocis.ezbocis_blueprint import ezbocis
import os

'''
ezcontroll Service
'''
@ezbocis.route("/ezcontrol")
def ezcontrol():
	return render_template("ezcontrol.html")
