from flask.ext.mail import Message
from hello import mail, app
msg = Message('test subject', sender='272251416@qq.com', recipients=['a272251416@gmail.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'

with app.app_context():
    mail.send(msg)
