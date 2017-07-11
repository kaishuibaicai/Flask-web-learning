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
1、结构图
[项目结构图](http://ww1.sinaimg.cn/large/bd31b54fgy1fh9gmmd1jxj20pf0pdmy1.jpg)

2、构建相同环境的包

Flask==0.10.1     [Flask web框架](http://docs.jinkan.org/docs/flask/)

Flask-Bootstrap==3.0.3.1     [推特开源框架](http://flask-bootstrap-zh.readthedocs.io/zh/latest/)

Flask-Mail==0.9.0     [Flask 邮件](https://pythonhosted.org/Flask-Mail/)

Flask-Migrate==1.1.0     [管理升级迁移数据库](https://www.google.com.hk/search?q=Flask-Migrate&rlz=1C1CHZL_zh-cnUS713US713&oq=Flask-Migrate&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8&gws_rd=cr,ssl)

Flask-Moment==0.2.0     [轻量级JavaScript日起处理类库](https://github.com/miguelgrinberg/Flask-Moment)

Flask-SQLAlchemy==1.0     [数据库管理](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)

Flask-Script==0.6.6     [Flask应用命令行解析器](https://github.com/nummy/flask-script-cn)

Flask-WTF==0.9.4     [基于Flask 的WTForms 集成](http://docs.jinkan.org/docs/flask-wtf/)

Jinja2==2.7.1     [Jinja2 是一个 Python 的功能齐全的模板引擎](http://docs.jinkan.org/docs/jinja2/)

Mako==0.9.1     [Mako模板库](http://www.makotemplates.org/)

MarkupSafe==0.18     [MarkupSafe是一个用于Python的库，它实现了一个识别HTML转义规则的unicode字符串，可用于实现自动字符串转义。它由Jinja 2，Mako模板引擎，Pylons Web框架等等使用。](http://www.pocoo.org/projects/markupsafe/)

SQLAlchemy==0.8.4     [SQLAlchemy是Python SQL工具包和对象关系映射器，为应用程序开发人员提供了SQL的全部功能和灵活性。](https://www.sqlalchemy.org/)

WTForms==1.0.5     [表单处理模块](http://docs.jinkan.org/docs/flask/patterns/wtforms.html)

Werkzeug==0.9.4     [Werkzeug是一个WSGI工具包，他可以作为一个Web框架的底层库](http://werkzeug-docs-cn.readthedocs.io/zh_CN/latest/) 计算密码散列值并进行核对

alembic==0.6.2     [Alembic是用于Python的SQLAlchemy数据库工具包的轻量级数据库迁移工具。](http://alembic.zzzcomputing.com/en/latest/)

blinker==1.3     [Blinker 是一个基于Python的强大的信号库，它既支持简单的对象到对象通信，也支持针对多个对象进行组播。Flask的信号机制就是基于它建立的。](http://python.jobbole.com/85554/)

itsdangerous==0.23     [有时候你想向不可信的环境发送一些数据，但如何安全完成这个任务呢？解决的方法就是签名。使用只有你自己知道的密钥，来加密签名你的数据，并把加密后的数据发给别人。当你取回数据时，你就可以确保没人篡改过这份数据。](http://itsdangerous.readthedocs.io/en/latest/) 生成并核对加密安全令牌


# 问题解决 

问题解决1：第五章，python hello.py shell 并没有进入命令行界面，而是直接运行，[这里](http://cocode.cc/t/python-flask-app-py-shell-command-lile/5846)解决了这个问题.

问题解决2： 第六章， 在设置邮件用户名和密码之后，如果关闭当前窗口，重新打开后需要重新设置。[参考](http://cocode.cc/t/flask-web-python-shell-errno-10060/3508/23)

问题解决3： 第六章，“warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future. Set it to True to suppress this warning.')”  [参考](http://cocode.cc/t/flask-web-flask-sqlalchemy/3443)

