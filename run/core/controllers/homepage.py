#!/usr/bin/env python3

from flask import Blueprint, render_template


controller = Blueprint('homepage', __name__, url_prefix='/homepage')


@controller.route('/homepage', methods=['GET'])
def homepage():
    return render_template('homepage.html')
