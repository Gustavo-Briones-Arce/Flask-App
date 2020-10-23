from sqlalchemy.orm import backref
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'admin_usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)
    grupos = db.relationship('Grupo', secondary='admin_usuario_grupo')

    def __repr__(self):
        return f'<Usuario {self.email}>'

    def set_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    def get_contrasena(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def get_by_id(_id):
        return Usuario.query.get(_id)

    @staticmethod
    def get_by_email(_email):
        return Usuario.query.filter_by(email=_email).first()


class Grupo(db.Model):
    __tablename__ = 'admin_grupo'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(15), nullable=False)
    descripcion = db.Column(db.String(100))
    usuarios = db.relationship('Usuario', secondary='admin_usuario_grupo')
    menus = db.relationship('Menu', secondary='admin_grupo_menu')

    def save(self):
        db.session.add(self)
        db.session.commit()

class Usuario_Grupo(db.Model):
    __tablename__ = 'admin_usuario_grupo'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('admin_usuario.id'))
    grupo_id = db.Column(db.Integer, db.ForeignKey('admin_grupo.id'))

class Menu(db.Model):
    __tablename__ = 'admin_menu'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(15), nullable=False)
    grupos = db.relationship('Grupo', secondary='admin_grupo_menu')

class Grupo_Menu(db.Model):
    __tablename__ = 'admin_grupo_menu'

    id = db.Column(db.Integer, primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('admin_grupo.id'))
    menu_id = db.Column(db.Integer, db.ForeignKey('admin_menu.id'))


