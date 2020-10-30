from app import db

class Base_Contable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sesion = db.Column(db.String(15), nullable=False)
    id_division = db.Column(db.String(11), nullable=False)
    meet = db.Column(db.Integer, nullable=False)
    reunion = db.Column(db.Integer, nullable=False)
    venta = db.Column(db.Integer, default=0)
    venta_aw = db.Column(db.Integer, default=0)
    cancelacion = db.Column(db.Integer, default=0)
    cancelacion_aw = db.Column(db.Integer, default=0)
    devolucion = db.Column(db.Integer, default=0)
    devolucion_aw = db.Column(db.Integer, default=0)
    pago = db.Column(db.Integer, default=0)
    apertura = db.Column(db.Integer, default=0)
    cierre =  db.Column(db.Integer, default=0)
    deposito = db.Column(db.Integer, default=0)
    retiro = db.Column(db.Integer, default=0)
    