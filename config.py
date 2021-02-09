import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY')


class TestConfig(BaseConfig):
    DEBUG = True
