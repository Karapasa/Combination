from flask import Flask
from config import BaseConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(BaseConfig)
bootstrap = Bootstrap(app)

from app import views