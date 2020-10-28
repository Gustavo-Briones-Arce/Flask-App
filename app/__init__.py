from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_module='config.config'):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    Bootstrap(app)

    from .admin import admin
    app.register_blueprint(admin)

    from .mantenedores import mantenedores
    app.register_blueprint(mantenedores)

    return app