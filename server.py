#!/usr/bin/python3
from flup.server.fcgi import WSGIServer
from flask_gpio.application import app
if __name__== '__main__':
    WSGIServer(app).run()
