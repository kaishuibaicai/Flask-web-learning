from flask import Flask    # 导入flask模块的Flask方法
from flask import request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)      # 实例化一个网络应用，这里的__name__参数是传递给Flask程序，决定程序的根目录，以便稍后能找到相对于程序跟目录的资源文件位置
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')            # Flask程序的的装饰器
def index():               # 视图函数，返回包含HTML的代码
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, %s</h1><h2>Your browser is %s' % (name, user_agent)

if __name__ == '__main__':
    manager.run()
