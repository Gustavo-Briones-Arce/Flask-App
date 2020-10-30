from __future__ import division
from app.mantenedores.models import Asociacion, Comunidad, Division, Meet
from . import mantenedores
from app import login_manager
from .forms import *
from flask import flash, render_template

@mantenedores.route('/meet/nuevo', methods=['GET', 'POST'])
def meet_nuevo():
    form = MeetForm()
    if form.validate_on_submit():
        meet = Meet()
        meet.nombre = form.nombre.data
        meet.save()
        flash('Meet Guardado', 'ok')
    return render_template('mantenedores/form.html', title='Nuevo Meet', form=form)

@mantenedores.route('/asociacion/nuevo', methods=['GET', 'POST'])
def asociacion_nuevo():
    form = AsociacionForm()
    if form.validate_on_submit():
        asociacion = Asociacion()
        asociacion.nombre = form.nombre.data
        asociacion.save()
        flash('Asociación Guardada', 'ok')
    return render_template('mantenedores/form.html', title='Nueva Asociación', form=form)

@mantenedores.route('/comunidad/nuevo', methods=['GET', 'POST'])
def comunidad_nuevo():
    form = ComunidadForm()
    if form.validate_on_submit():
        comunidad = Comunidad()
        comunidad.asociacion_id = form.asociacion.data.id
        comunidad.comunidad_id = form.comunidad.data
        comunidad.nombre = form.nombre.data
        comunidad.save()
        flash('Comunidad Guardada', 'ok')
    return render_template('mantenedores/form.html', title='Nueva Comunidad', form=form)

@mantenedores.route('/division/nuevo', methods=['GET', 'POST'])
def division_nuevo():
    form = DivisionForm()
    if form.validate_on_submit():
        division = Division()
        division.comunidad_id = form.comunidad.data.id
        division.division_id = form.division.data
        division.nombre = form.nombre.data
        division.save()
        flash('Asociación Guardada', 'ok')
    return render_template('mantenedores/form.html', title='Nueva División', form=form)

@mantenedores.route('/zona_participacion/nuevo', methods=['GET', 'POST'])
def zona_participacion_nuevo():
    form = ZonaParticipacionForm()
    if form.validate_on_submit():
        zona_participacion = ZonaParticipacion()
        if form.grupo_zona.data:
            zona_participacion.grupo_zona_id = form.grupo_zona.data.id
        else:
            zona_participacion.grupo_zona_id = None
        zona_participacion.nombre = form.nombre.data
        zona_participacion.vta_neta = form.vta_neta.data
        zona_participacion.gto_explotacion = form.gto_explotacion.data
        zona_participacion.unico = form.unico.data
        zona_participacion.save()
        flash('Zona de Partición Guardada', 'ok')
    return render_template('mantenedores/form.html', title='Nueva Zona Participación', form=form)

