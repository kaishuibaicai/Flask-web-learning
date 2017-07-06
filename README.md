# 《Flask Web 开发》学习笔记

[TOC]

## 一、程序的基本结构

### 1、flask的安装：

为了避免系统的Python解释器中的包的混乱，这里可以另外做一个Python的虚拟环境，在虚拟环境中安装的包是独立的：

```
$ sudo apt-get install python-virtualenv
```

在开发的独立文件夹中创建虚拟环境：

```
$ virtualenv venv     # venv是虚拟环境的名称
```

启动虚拟环境：

```
$ source venv/bin/activate
```

关闭虚拟环境：

```
$ deactivate
```

在虚拟环境中安装Flask包：

```
$ pip3 install flask
```


## 2.Hello World

实现一个最简单的**网络应用**

```
  1 from flask import Flask    # 导入flask模块的Flask方法
  2 from flask import request
  3 app = Flask(__name__)      # 实例化一个网络应用，这里的__name__参数是传递给Flask程序，决定程序的根目录，以便稍后能找到相对于程序跟目录的资源文件位置
  4 
  5 @app.route('/')            # Flask程序的的装饰器
  6 def index():               # 视图函数，返回包含HTML的代码
  7     return '<h1>Hello World!</h1>'
  8 
  9 @app.route('/user/<name>')
 10 def user(name):
 11     user_agent = request.headers.get('User-Agent')
 12     return '<h1>Hello, %s</h1><h2>Your browser is %s' % (name, user_agent)
 13 
 14 if __name__ == '__main__':
 15     app.run(debug=True)                                                                                                         
```

## 七、项目结构

![项目结构图](http://ww1.sinaimg.cn/large/bd31b54fgy1fh9gmmd1jxj20pf0pdmy1.jpg)

# 问题解决 

问题解决1：第五章，python hello.py shell 并没有进入命令行界面，而是直接运行，[这里](http://cocode.cc/t/python-flask-app-py-shell-command-lile/5846)解决了这个问题.

问题解决2： 第六章， 在设置邮件用户名和密码之后，如果关闭当前窗口，重新打开后需要重新设置。[参考](http://cocode.cc/t/flask-web-python-shell-errno-10060/3508/23)



