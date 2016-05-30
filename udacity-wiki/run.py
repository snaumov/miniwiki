__author__ = 'stepan'

from app import app
from models import db
from pages import pages
# from loginpage import loginpage
#
#
app.register_blueprint(pages)
# app.register_blueprint(loginpage)


if __name__ == '__main__':
    app.run(host='0.0.0.0')