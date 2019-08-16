import math


class Config:
    SHAPES = {
        'cylinder': {
            'dimensions': ['height', 'radius'],
            'volume_func': lambda h, r: math.pi*r*r*h,
            'area_func': lambda h, r: 2 * math.pi*r*(r + h)
        },
        'cone': {
            'dimensions': ['height', 'radius'],
            'volume_func': lambda h, r: math.pi*r*r*h / 3,
            'area_func': lambda h, r: math.pi*r*(r + math.sqrt(h*h + r*r))
        },
        'cuboid': {
            'dimensions': ['length', 'breadth', 'height'],
            'volume_func': lambda l, b, h: l*b*h,
            'area_func': lambda l, b, h: 2 * (l*b + b*h + l*h)
        }
    }

    MATERIALS = {
        'iron': {
            'price': 2
        },
        'steel': {
            'price': 1
        }
    }

    COATINGS = {
        'gold': {
            'price': 1000
        },
        'silver': {
            'price': 100
        },
        'copper': {
            'price': 10
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
