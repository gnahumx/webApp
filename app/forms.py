from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Persona(FlaskForm):
    Nombre = StringField('Nombre', validators=[DataRequired(), Length(max=64, min=4)])
    Genero = StringField('Genero', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    #password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
