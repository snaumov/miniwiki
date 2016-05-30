__author__ = 'snaumov'


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SET, VARCHAR, DATE, FLOAT, NUMERIC, TEXT
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)



class Pages(db.Model):
    __tablename__ = 'Pages'
    id = db.Column(INTEGER, primary_key=True, autoincrement=True)
    PageName = db.Column(TEXT)
    PageContent = db.Column(TEXT)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(INTEGER, primary_key=True, autoincrement=True)
    Username = db.Column(TEXT)
    Password = db.Column(TEXT)

class PageHistory(db.Model):
    __tablename__ = 'PageHistory'
    id = db.Column(INTEGER, primary_key=True, autoincrement=True)
    page_id = db.Column(db.Integer, db.ForeignKey('Pages.id'))
    content_added = db.Column(TEXT)
    content_removed = db.Column(TEXT)
    currentcontent = db.Column(TEXT)
    dateofchange = db.Column(DATE)
