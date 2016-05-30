__author__ = 'snaumov'

from flask_wtf import Form
from wtforms import BooleanField, StringField, validators, DateTimeField, IntegerField, FileField, TextAreaField


class Page(Form):
    PageContent = TextAreaField('PageContent', [validators.Length(min=3, max=100000, message='Enter your text')])



