from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Persona(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64, min=4)])
    genero = StringField('Genero', validators=[DataRequired(), Length(max=9, min=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
