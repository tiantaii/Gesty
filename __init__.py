import os
from flask import Flask

def create_app():
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configurar la aplicación
    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    # Importar e inicializar el módulo de base de datos
    from . import db
    db.init_app(app)

    from . import auth
    app.register.blueprint(auth.bp)

    # Definir una ruta
    @app.route('/testing')
    def testing():
        return 'testing'

    # Retornar la instancia de la aplicación
    return app
