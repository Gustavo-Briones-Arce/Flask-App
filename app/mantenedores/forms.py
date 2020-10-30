from .models import *
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

def choice_Asociacion():
    return Asociacion.query.all()

def choice_Comunidad():
    return Comunidad.query.all()

def choice_Zona_Distribucion():
    return ZonaDistribucion.query.all()

def choice_Zona_Simulcasting():
    return ZonaSimulcasting.query.all()

def choice_Zona_Participacion():
    return ZonaParticipacion.query.all()

def choice_Asociado():
    return TipoAsociado.query.all()

def choice_Categoria():
    return DivisionCategoria.query.all()

def choice_Encargado():
    return Encargado.query.all()

def choice_Grupo_Zona_Participacion():
    return GrupoZonaParticipacion.query.all()


class MeetForm(FlaskForm):
    nombre = StringField('Nombre Meet', validators=[DataRequired('Ingrese Nombre'), Length(min=5)])
    boton = SubmitField('Ingresar')

class AsociacionForm(FlaskForm):
    nombre = StringField('Nombre Asociación', validators=[DataRequired('Ingrese Nombre'), Length(min=5)])
    boton = SubmitField('Ingresar')

class ComunidadForm(FlaskForm):
    asociacion = QuerySelectField('Asociación', query_factory=choice_Asociacion, get_label='nombre', allow_blank=True, blank_text='Seleccione Asociación')
    comunidad = IntegerField('N° Comunidad', validators=[InputRequired('Ingrese Numero'), NumberRange(min=0, max=99)])
    nombre = StringField('Nombre Asociación', validators=[DataRequired('Ingrese Nombre'), Length(min=5)])
    boton = SubmitField('Ingresar')

class DivisionForm(FlaskForm):
    comunidad = QuerySelectField('Comunidad', query_factory=choice_Comunidad, allow_blank=True, blank_text='Seleccione Comunidad')
    division = IntegerField('N° División', validators=[InputRequired('Ingrese Numero'), NumberRange(min=0, max=99)])
    nombre = StringField('Nombre División', validators=[DataRequired('Ingrese Nombre'), Length(min=5)])
    zona_distribucion = QuerySelectField('Zona de Distribución', query_factory=choice_Zona_Distribucion, get_label='', allow_blank=True, blank_text='')
    zona_simulcasting = QuerySelectField('Zona de Simulcasting', query_factory=choice_Zona_Simulcasting, get_label='', allow_blank=True, blank_text='')
    zona_participacion = QuerySelectField('Zona de Partipación', query_factory=choice_Zona_Participacion, get_label='', allow_blank=True, blank_text='')
    tipo_asociado = QuerySelectField('Tipo Asociado', query_factory=choice_Asociacion, get_label='', allow_blank=True, blank_text='')
    categoria = QuerySelectField('Categoria de la División', query_factory=choice_Categoria, get_label='', allow_blank=True, blank_text='')
    encargado = QuerySelectField('Encargado', query_factory=choice_Encargado, get_label='', allow_blank=True, blank_text='')
    boton = SubmitField('Ingresar')


class GrupoZonaParticipacionForm(FlaskForm):
    nombre = StringField('Nombre Grupo', validators=[DataRequired('Ingrese Nombre'), Length(min=5)])
    glosa = StringField('Glosa', validators=[Length(max=6)])
    glosa_3 = StringField('Glosa Reporte 3%', validators=[DataRequired('Ingrese glosa'), Length(min=5)])
    boton = SubmitField('Ingresar')


class ZonaParticipacionForm(FlaskForm):
    grupo_zona = QuerySelectField('Grupo de Zona de Ṕarticipación', query_factory=choice_Grupo_Zona_Participacion, get_label='', allow_blank=True, blank_text='')
    nombre = StringField('Nombre Zona', validators=[DataRequired('Ingrese Nombre'), Length(min=5)])
    vta_neta = DecimalField('% de la Venta Neta', validators=[InputRequired('Ingrese valor')], places=2)
    gto_explotacion = DecimalField('% del Gasto de Explotación', validators=[InputRequired('Ingrese valor')], places=2)
    unico = DecimalField('% Unico', validators=[InputRequired('Ingrese valor')], places=2)
    boton = SubmitField('Ingresar')

