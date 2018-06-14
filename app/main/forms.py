#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required



class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])#保证字段不为空
    submit = SubmitField('Submit')