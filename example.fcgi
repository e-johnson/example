#!/HOMEDIR/USERNAME/venv/flask_hello_world/bin/python

from flup.server.fcgi import WSGIServer
from flask_hello_world_app import app as application

WSGIServer(application).run()