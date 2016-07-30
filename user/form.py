from flask_wtf import Form
from wtforms import EmailField, validators
from wtforms.fields.html5 import EmailField

class UserForm(Form):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
