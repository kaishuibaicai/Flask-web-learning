#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User
from flask.ext.pagedown.fields import PageDownField


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[Required(), Length(1, 64)])
    confirmed = BooleanField('认证')
    role = SelectField('角色', coerce=int)
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')


    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱地址已经被注册了')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise validationError('用户名已经被使用了')


class PostForm(FlaskForm):
    body = PageDownField("你的想法是什么？", validators=[Required()])
    submit = SubmitField('提交')


class CommentForm(FlaskForm):
    body = StringField('', validators=[Required()])
    submit = SubmitField('提交')
