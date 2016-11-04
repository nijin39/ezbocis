# -*- coding: utf-8 -*-

from flask import Blueprint
from ezbocis.ezbocis_logger import Log

ezbocis = Blueprint('ezbocis', __name__,
                     template_folder='../templates', static_folder='../static')

Log.info('static folder : %s' % ezbocis.static_folder)
Log.info('template folder : %s' % ezbocis.template_folder)
