import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><center> Hello World! </center></h1>"





if __name__ == '__main__':
    host=os.getenv('FLASK_HOST', '0.0.0.0')
    port=os.getenv('FLASK_PORT', '8000')
    app.run(host=host, port=port)