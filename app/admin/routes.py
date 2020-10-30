from app import login_manager
from . import admin
from flask import render_template, redirect, flash, url_for, request
from .forms import LoginForm, RegistroForm, GrupoForm, UsuarioEditForm
from .models import Grupo, Usuario

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario().get_by_email(form.email.data)
        if usuario:
            if usuario.get_contrasena(form.contrasena.data):
                return 'Bienvenido'
            else:
                flash('Contraseña Incorrecta', 'error')
        else:
            flash('Usuario Incorrecto', 'error')

    return render_template('admin/form.html', form=form, title='Login')

@admin.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        usuario = Usuario()
        usuario.nombre = form.nombre.data
        usuario.email = form.email.data
        usuario.set_contrasena(form.contrasena.data)
        usuario.save()
        flash('Registro Exitoso!', 'ok')
        return redirect(url_for('admin.login'))
    
    return render_template('admin/form.html', form=form, title='Registro')

@admin.route('/grupos/nuevo', methods=['GET', 'POST'])
def grupo_nuevo():
    form = GrupoForm()
    if form.validate_on_submit():
        grupo = Grupo()
        grupo.nombre = form.nombre.data
        grupo.descripcion = form.descripcion.data
        grupo.save()
        flash('Grupo creado', 'ok')
    return render_template('admin/form.html', form=form, title='Crear Grupo')

@admin.route('/usuarios',  methods=['GET', 'POST'])
def usuarios():
    usuarios = Usuario.query.order_by(Usuario.nombre)
    return render_template('admin/listUsuarios.html', title='Usuarios', usuarios=usuarios)

@admin.route('/usuarios/<int:id>/editar', methods=['GET', 'POST'])
def usuario_editar(id):
    usuario = Usuario.query.get_or_404(id)
    if usuario:
        form = UsuarioEditForm(obj=usuario)

        if form.validate_on_submit():
            usuario.nombre = form.nombre.data
            usuario.email = form.email.data
            usuario.contrasena = form.contrasena.data
            
            act_grupos = tuple(usuario.grupos)
            for act_grupo in act_grupos:
                if act_grupo not in form.grupos.data:
                    if act_grupo.nombre == 'Administradores':
                        usuario.es_admin = False
                    usuario.grupos.remove(act_grupo)

            for sel_grupo in form.grupos.data:
                if sel_grupo not in act_grupos:
                    if sel_grupo.nombre == 'Administradores':
                        usuario.es_admin = True
                    usuario.grupos.append(sel_grupo)
            usuario.save()
            flash('Usuario Actualizado', 'ok')
        elif request.method == 'GET':
            form.nombre.data = usuario.nombre
            form.email.data = usuario.email
            form.contrasena.data = usuario.contrasena
        return render_template('admin/form.html', form=form)
    else:
        flash('Usuario no Existe', 'error')

@admin.route('/grupos')
def grupos():
    return render_template('admin/listGrupo.html')

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(int(user_id))
