from sqlalchemy.orm import backref
from sqlalchemy.sql import func
from app import db


class Asociacion(db.Model):
    __tablename__ = 'mantenedores_asociacion'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    comunidades = db.relationship('Comunidad', backref='mantenedores_asociacion', lazy=True)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class Comunidad(db.Model):
    __tablename__ = 'mantenedores_comunidad'

    id = db.Column(db.Integer, primary_key=True)
    asociacion_id = db.Column(db.Integer, db.ForeignKey('mantenedores_asociacion.id'))
    comunidad_id = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    divisiones = db.relationship('Division', backref='mantenedores_comunidad', lazy=True)

    def __repr__(self) -> str:
        asociacion = Asociacion.query.filter(Asociacion.id==self.asociacion_id).first()
        return asociacion.nombre + ' - ' + self.nombre

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class Division(db.Model):
    __tablename__ = 'mantenedores_division'

    id = db.Column(db.Integer, primary_key=True)
    comunidad_id = db.Column(db.Integer, db.ForeignKey('mantenedores_comunidad.id'))
    division_id = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    zona_distribucion_id = db.Column(db.Integer, db.ForeignKey('mantenedores_zona_distribucion.id'), nullable=False)
    zona_simulcasting_id = db.Column(db.Integer, db.ForeignKey('mantenedores_zona_simulcasting.id'), nullable=False)
    zona_participacion_id = db.Column(db.Integer, db.ForeignKey('mantenedores_zona_participacion.id'), nullable=False)
    tipo_asociado_id = db.Column(db.Integer, db.ForeignKey('mantenedores_tipo_asociado.id'), nullable=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('mantenedores_division_categoria.id'), nullable=True)
    encargado_id = db.Column(db.Integer, db.ForeignKey('mantenedores_encargado.id'), nullable=True)
    estado = db.Column(db.Boolean, default=0)
    division = db.Column(db.String(11), nullable=False)

    def set_division(self):
        comunidad = Comunidad.query.filter(Comunidad.id==self.comunidad_id).first()
        asociacion = Asociacion.query.filter(Asociacion.id==comunidad.asociacion_id).first()
        aso = '000' + str(asociacion.id)
        com = '000' + str(comunidad.comunidad_id)
        div = '000' + str(self.division_id)
        self.division = aso[-3:] + '.' + com[-3:] + '.' + div[-3:]

    def save(self):
        if not self.id:
            self.set_division()
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class GrupoZonaParticipacion(db.Model):
    __tablename__ = 'mantenedores_grupo_zona_participacion'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    glosa = db.Column(db.String(6), nullable=True)
    glosa_3_porciento = db.Column(db.String(25), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class ZonaParticipacion(db.Model):
    __tablename__ = 'mantenedores_zona_participacion'

    id = db.Column(db.Integer, primary_key=True)
    grupo_zona_id = db.Column(db.Integer, db.ForeignKey('mantenedores_grupo_zona_participacion.id'))
    nombre = db.Column(db.String(50), nullable=False)
    vta_neta = db.Column(db.Numeric, default=0)
    gto_explotacion = db.Column(db.Numeric, default=0)
    unico = db.Column(db.Numeric, default=0)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class ZonaParticipacionTramo(db.Model):
    __tablename__ = 'mantenedores_zona_participacion_tramo'

    id = db.Column(db.Integer, primary_key=True)
    zona_participacion_id = db.Column(db.Integer, db.ForeignKey('mantenedores_zona_participacion.id'), nullable=False)
    tramo = db.Column(db.Integer, nullable=False)
    vta_final = db.Column(db.Integer, nullable=False)
    participacion = db.Column(db.Numeric, default=0)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class ZonaSimulcasting(db.Model):
    __tablename__ = 'mantenedores_zona_simulcasting'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class ZonaDistribucion(db.Model):
    __tablename__ = 'mantenedores_zona_distribucion'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class TipoEncargado(db.Model):
    __tablename__ = 'mantenedores_tipo_encargado'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Boolean, default=0)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class Encargado(db.Model):
    __tablename__ = 'mantenedores_encargado'

    id = db.Column(db.Integer, primary_key=True)
    tipo_encargado = db.Column(db.Integer, db.ForeignKey('mantenedores_tipo_encargado.id'))
    rut = db.Column(db.Integer, nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Boolean, default=0)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class TipoAsociado(db.Model):
    __tablename__ = 'mantenedores_tipo_asociado'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class DivisionCategoria(db.Model):
    __tablename__ = 'mantenedores_division_categoria'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Boolean, default=0)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class Meet(db.Model):
    __tablename__ = 'mantenedores_meet'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class Sesion(db.Model):
    __tablename__ = 'mantenedores_sesion'

    sesion = db.Column(db.String(13), primary_key=True)
    nro_sesion = db.Column(db.Integer, nullable=False)
    fecha_sesion = db.Column(db.Date, nullable=False)
    fecha_carga = db.Column(db.Date, nullable=False)
    disco = db.Column(db.String(1), nullable=False)
    fecha_creacion = db.Column(db.Date, default=func.now())
    fecha_proceso = db.Column(db.Date, nullable=True)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()


class SesionDetalle(db.Model):
    __tablename__ = 'mantenedores_sesion_detalle'

    id = db.Column(db.Integer, primary_key=True)
    sesion = db.Column(db.String(13), db.ForeignKey('mantenedores_sesion.sesion'), nullable=False)
    meet = db.Column(db.Integer, db.ForeignKey('mantenedores_meet.id'), nullable=False)
    administrador = db.Column(db.Integer, nullable=False)
    operador = db.Column(db.Integer, nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()

