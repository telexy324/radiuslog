from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional, IPAddress, DataRequired
from wtforms import ValidationError
from .. import utils


class IpQueryForm(FlaskForm):
    ipaddress = StringField('IP', validators=[IPAddress(message='IP Format is not correct, Please check again!')])
    #blimit = DateTimeField('StartDate', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    #tlimit = DateTimeField('EndDate', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    blimit = StringField('StartDate', validators=[DataRequired(message='Please fullfill this field using datetimepicker!'), Length(0, 64)])
    tlimit = StringField('EndDate', validators=[DataRequired(message='Please fullfill this field using datetimepicker!'), Length(0, 64)])
    submit = SubmitField('Search')


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])