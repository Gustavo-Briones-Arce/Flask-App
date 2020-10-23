from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from .models import Grupo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=5, max=65)])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5)])
    boton = SubmitField('Ingresar')

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired(), Length(min=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    contrasena2 = PasswordField('Repita Contraseña', validators=[DataRequired(), EqualTo('contrasena', 'Las contraseñas no coinciden')])
    boton = SubmitField('Registrarse')

class GrupoForm(FlaskForm):
    nombre = StringField('Nombre del Grupo', validators=[DataRequired(), Length(min=5)])
    descripcion = TextAreaField('Descripción')
    boton = SubmitField('Crear')

class UsuarioEditForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired(), Length(min=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    grupos = SelectMultipleField('Grupo(s)')
    boton = SubmitField('Actualizar!')



