from flask import Flask
import os
from config import DevelopmentConfig

app = Flask(__name__)


app.config.from_object(DevelopmentConfig)
from core import routes