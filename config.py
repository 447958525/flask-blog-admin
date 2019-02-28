from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask
    CSRF_ENABLED = True
    SECRET_KEY = '123456'
    WTF_CSRF_SECRET_KEY = 'random key for form'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASKY_MAIL_SENDER = 'Flask Admin <447958525@qq.com>'
    FLASKY_ADMIN = '447958525@qq.com'
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 10
    FLASKY_COMMENTS_PER_PAGE = 10

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = '447958525@qq.com'
    MAIL_PASSWORD = 'fycgrmfdrzlobjje'

    UPLOAD_FOLDER = os.getcwd() + '/app/static/images/'
    #UPLOAD_FOLDER_PHOTOS = os.getcwd() + '/app/static/fonts/'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
                fromaddr=cls.FLASKY_MAIL_SENDER,
                toaddrs=cls.FLASKY_MAIL_SUBJECT_PREFIX + 'Application Error',
                credentials=credentials,
                secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)



