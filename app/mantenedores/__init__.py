from flask import Blueprint

mantenedores = Blueprint('mantenedores', __name__, template_folder='templates', url_prefix='/mantenedores')

from . import routes