#!/usr/bin/env python3
# -*- coding: utf8 -*-
""""Simple flask app"""
from flask import Flask #from the flask package
                        #import the Flask class
app = Flask(__name__) #Instantiate Flask into the "app" variable

from app import routes