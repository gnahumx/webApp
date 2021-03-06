from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Persona(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired( message="El campo es obligatorio."), Length(max=64, min=4, message="El campo debe tener entre 4 y 10 caracteres.")])
    lugar = StringField("Lugar", validators=[DataRequired( message="El campo es obligatorio."), Length(max=64, min=5, message="El campo debe tener entre 4 y 10 caracteres.")])
    genero = StringField("Genero", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired("El campo es obligatorio."), Email( message="Introduzca una dirección de correo válida.")])
    #password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


