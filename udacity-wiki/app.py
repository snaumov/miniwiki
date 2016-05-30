__author__ = 'snaumov'


import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for, Response
from flask_bootstrap import Bootstrap



APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
Bootstrap(app)


