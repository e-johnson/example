from datetime import datetime
from flask import Flask
app = Flask(__name__)
def strip_url(orig):
   return orig.replace('index.fcgi/', '')

@app.route('/')
def hello_world():
    return strip_url('Hello World!')

@app.route('/the-time')
def the_time():
     cur_time = str(datetime.now())
     return cur_time + ' is the current time!  ...YEAH!'

if __name__ == '__main__':
    app.run()