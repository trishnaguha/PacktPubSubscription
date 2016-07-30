from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./user/templates', static_folder='./user/static')
app.config.from_object('settings')
db = SQLAlchemy(app)

from user import views
