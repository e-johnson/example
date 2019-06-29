#!/usr/local/bin/python3

from flup.server.fcgi import WSGIServer
from flask_hello_world_app import app as application

WSGIServer(application).run()