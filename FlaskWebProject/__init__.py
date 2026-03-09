import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Configure Session
Session(app)

# Initialize Database
db = SQLAlchemy(app)

# Initialize Login Manager
login = LoginManager(app)
login.login_view = 'login'

# Configure Logging
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('CMS Application startup')

# Import views at the end to avoid circular imports
from FlaskWebProject import views
