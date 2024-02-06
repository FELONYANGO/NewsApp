class Config(object):
    SECRET_KEY = 'gues_me'
    DEBBUG =False
    TESTING = False
    CSRF_ENABLE = True


class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
