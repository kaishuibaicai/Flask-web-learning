from flask import make_response
from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
@app.route('/re')
def redi():
    return redirect('http://www.baidu.com')

if __name__ == '__main__':
    app.run(debug=True)
