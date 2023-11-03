class Config:
    """
    Base configuration class.
    """
    MODEL_PATH = 'models/model1.pkl'
    PORT = 3000
    DEBUG = True  # Set to False in production


class ProductionConfig(Config):
    """
    Production-specific configuration.
    """
    DEBUG = False
    # Add production-specific configuration settings here


class DevelopmentConfig(Config):
    """
    Development-specific configuration.
    """
    DEBUG = True
    # Add development-specific configuration settings here


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': Config,
}
