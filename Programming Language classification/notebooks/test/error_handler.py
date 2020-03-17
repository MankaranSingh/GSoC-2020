from flask import render_template, jsonify
from .. import Error_handler

@Error_handler.app_errorhandler(404)
def page_not_found(e):
    return jsonify(error='404')
