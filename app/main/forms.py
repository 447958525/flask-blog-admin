#coding:utf-8
from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, SelectField, FileField
from wtforms.validators import Required, Email, Length, Regexp
from ..models import Role, User
from flask_pagedown.fields import PageDownField


class NameForm(Form):
    name = StringField('你要说点什么吗?', validators=[Required()])
    submit = SubmitField('提交')


class EditProfileForm(Form):
    name = StringField('你的真名', validators=[Length(0, 64)])
    location = StringField('地区', validators=[Length(0, 64)])
    about_me = TextAreaField('关于的说明')
    submit = SubmitField('提交')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Username must have only letters,'
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Real name', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(Form):
    body = PageDownField("What's on your mind?",  validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(Form):
    body = StringField('发表你的评论', validators=[Required()])
    submit = SubmitField('提交')


class EditAvatarForm(Form):
    avatar = FileField('修改您的头像')
    submit = SubmitField('提交')


class DeletePostForm(Form):
    NotDelete = StringField('取消')
    submit = SubmitField('确定删除')


