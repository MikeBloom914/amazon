#!/usr/bin/env python3

from flask import Flask, Blueprint, redirect, render_template, request, url_for

controller = Blueprint('login', __name__, url_prefix='')


@controller.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']

        if email != 'mikebloom914@gmail.com' or password != 'swordfish':
            return render_template('login.html', message='BAD CREDENTIALS...Please try again')
        else:
            return render_template('homepage.html')


@controller.route('/homepage', methods=['GET'])
def homepage():
    return render_template('homepage.html')
