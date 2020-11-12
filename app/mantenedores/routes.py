from flask.globals import request
from . import mantenedores
from app import login_manager
from .forms import *
from flask import flash, render_template, redirect, url_for


#METODOS PARA MEET
@mantenedores.route('/meet')
@mantenedores.route('/meet/')
def meets():
    meets = Meet.query.all()
    return render_template('mantenedores/meets.html', title='Meets', meets=meets)

@mantenedores.route('/meet/<int:id>')
@mantenedores.route('/meet/<int:id>/')
def meet(id):
    meet = Meet.query.get_or_404(id)
    return render_template('mantenedores/meet.html', title='Meet', meet=meet)

@mantenedores.route('/meet/nuevo', methods=['GET', 'POST'])
@mantenedores.route('/meet/nuevo/', methods=['GET', 'POST'])
def meet_nuevo():
    form = MeetForm()
    if form.validate_on_submit():
        meet = Meet()
        meet.nombre = form.nombre.data
        meet.save()
        flash('Meet Guardado', 'ok')
        return redirect(url_for('mantenedores.meets'))
    return render_template('mantenedores/form.html', title='Nuevo Meet', form=form)

@mantenedores.route('/meet/<int:id>/editar', methods=['GET', 'POST'])
@mantenedores.route('/meet/<int:id>/editar/', methods=['GET', 'POST'])
def meet_editar(id):
    meet = Meet.query.get_or_404(id)
    if meet:
        form = MeetForm()
        if form.validate_on_submit():
            meet.nombre = form.nombre.data
            meet.save()
            flash('Meet Editado', 'ok')
            return redirect(url_for('mantenedores.meets'))
        elif request.method == 'GET':
            form.nombre.data = meet.nombre
        return render_template('mantenedores/form.html', title='Editar Meet', form=form)

@mantenedores.route('/meet/<int:id>/eliminar')
@mantenedores.route('/meet/<int:id>/eliminar/')
def meet_eliminar(id):
    meet = Meet.query.get_or_404(id)
    if meet:
        meet.delete()
        flash('Meet Eliminado!', 'ok')
        return redirect(url_for('mantenedores.meets'))


#METODOS PARA ASOCIACION
@mantenedores.route('/asociacion')
@mantenedores.route('/asociacion/')
def asociaciones():
    asociaciones = Asociacion.query.all()
    return render_template('mantenedores/asociaciones.html', title='Asociaciones', asociaciones=asociaciones)

@mantenedores.route('/asociacion/<int:id>')
@mantenedores.route('/asociacion/<int:id>/')
def asociacion(id):
    asociacion = Asociacion.query.get_or_404(id)
    if asociacion:
        return render_template('mantenedores/asociacion.html', title='Asociación', asociacion=asociacion)

@mantenedores.route('/asociacion/nuevo', methods=['GET', 'POST'])
@mantenedores.route('/asociacion/nuevo/', methods=['GET', 'POST'])
def asociacion_nuevo():
    form = AsociacionForm()
    if form.validate_on_submit():
        asociacion = Asociacion()
        asociacion.nombre = form.nombre.data
        asociacion.save()
        flash('Asociación Guardada', 'ok')
        return redirect(url_for('mantenedores.asociaciones'))
    return render_template('mantenedores/form.html', title='Nueva Asociación', form=form)

@mantenedores.route('/asociacion/<int:id>/editar', methods=['GET', 'POST'])
@mantenedores.route('/asociacion/<int:id>/editar/', methods=['GET', 'POST'])
def asociacion_editar(id):
    asociacion = Asociacion.query.get_or_404(id)
    if asociacion:
        form = AsociacionForm()
        if form.validate_on_submit():
            asociacion.nombre = form.nombre.data
            asociacion.save()
            flash('Asociación Editada', 'ok')
            return redirect(url_for('mantenedores.asociaciones'))
        elif request.method == 'GET':
            form.nombre.data = asociacion.nombre
        return render_template('mantenedores/form.html', title='Editar Asociación', form=form)

@mantenedores.route('/asociacion/<int:id>/eliminar')
@mantenedores.route('/asociacion/<int:id>/eliminar/')
def asociacion_eliminar(id):
    asociacion = Asociacion.query.get_or_404(id)
    if asociacion:
        asociacion.delete()
        flash('Asociación Eliminada!', 'ok')
        return redirect(url_for('mantenedores.asociaciones'))
        

#METODOS PARA COMUNIDAD
@mantenedores.route('/comunidad/nuevo', methods=['GET', 'POST'])
@mantenedores.route('/comunidad/nuevo/', methods=['GET', 'POST'])
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

#METODOS PARA DIVICION
@mantenedores.route('/division/nuevo', methods=['GET', 'POST'])
@mantenedores.route('/division/nuevo/', methods=['GET', 'POST'])
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


#METODOS PARA ZONA DE PARTICIPACION
@mantenedores.route('/zona_participacion/nuevo', methods=['GET', 'POST'])
@mantenedores.route('/zona_participacion/nuevo/', methods=['GET', 'POST'])
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

