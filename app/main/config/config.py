"""Module defines the app configurations for the various environments."""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base config class that defines shared config variables."""

    DEBUG = False
    SECRET_KEY = os.environ["SECRET_KEY"]

    # DB related settings
    DB_URL = os.environ["DB_URL"]

    # Logging Configuration
    LOGGING_CONFIG = os.environ["LOGGING_CONFIG"]

    # Path to service info file
    SERVICE_INFO_PATH = os.environ.get("SERVICE_INFO_PATH", "../main/serviceInfo.json")


class DevelopmentConfig(BaseConfig):
    """Development Environment Config."""

    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing Environment Config."""

    DEBUG = True
    TESTING = True

    # Build the test mongo url
    DB_URL_PARTS = os.environ["DB_URL"].split("?")
    DB_URL = f"{DB_URL_PARTS[0]}_test?{DB_URL_PARTS[1]}"


class ProductionConfig(BaseConfig):
    """Production Environment Config."""

    DEBUG = False


CONFIG_BY_NAME = dict(development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig)

KEY = BaseConfig.SECRET_KEY
