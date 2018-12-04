from flask import render_template
from . import main


@main.app_errorhandler(404)
def errorPage(error):
    '''
    Function to render the 404 error errorPage
    '''
    return render_template('error.html'),404
