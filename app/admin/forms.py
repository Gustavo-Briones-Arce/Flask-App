from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
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

def choice_grupo():
    return Grupo.query.order_by(Grupo.nombre)

class UsuarioEditForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired(), Length(min=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contrasena = StringField('Contraseña', validators=[DataRequired()])
    grupos = QuerySelectMultipleField('Grupo(s)', query_factory=choice_grupo, get_label='nombre')
    boton = SubmitField('Actualizar!')

    def __init__(self, *args, **kwargs):
        kwargs['usuario'] = kwargs['obj']
        super(UsuarioEditForm, self).__init__(*args, **kwargs)
        self.grupos.default = lambda: kwargs['obj'].grupos

