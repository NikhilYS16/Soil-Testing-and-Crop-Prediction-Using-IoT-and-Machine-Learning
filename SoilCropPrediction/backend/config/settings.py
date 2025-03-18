# config/settings.py

class Config:
    DEBUG = True
    SECRET_KEY = 'supersecretkey'

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'your_production_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'your_secret_key'
    