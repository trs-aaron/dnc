import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
app.use_reloader = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import routes, models, errors, api

# Set up logging
# Format thx to Miguel Grinberg - e.g. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/events_app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Events API startup')
