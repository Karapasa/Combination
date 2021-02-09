from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Parametr(FlaskForm):
    name = StringField('Название параметра', validators=[DataRequired()])
    exceptions = StringField('Исключения', validators=[DataRequired()])
    submit = SubmitField('Сгенерировать данные')
