import math

class Config:
    APP_KEY = 'Something secret'

    SHAPES = {
        'cylender': {
            'params': ['height', 'radius'],
            'volume_func': lambda h, r: math.pi * r * r * h
        }
    }


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    DEBUG = False


configs = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
