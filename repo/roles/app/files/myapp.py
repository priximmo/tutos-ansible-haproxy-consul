#!/usr/bin/python
from flask import Flask
import socket
app = Flask(__name__)


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    message = "Bonjour, je suis " + hostname + "\n"
    return message

