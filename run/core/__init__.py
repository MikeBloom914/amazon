#!/usr/bin/env python3

import os

from flask import Flask

from core.controllers.login import controller as login


def keymaker(omnibus, filename='secret_key'):
    pathname = os.path.join(omnibus.instance_path, filename)
    print("Pathname", pathname)
    try:
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            os.system('mkdir -p {0}'.format(parent_directory))
        os.system('head -c 24 /dev/urandom > {0}'.format(pathname))
        omnibus.config['SECRET_KEY'] = open(pathname, filename)


omnibus = Flask(__name__)

omnibus.register_blueprint(login)

keymaker(omnibus)
