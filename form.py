from flask_wtf import Form
from wtforms import validators
from wtforms.field.html5 import EmailField

class UserForm(Form):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
