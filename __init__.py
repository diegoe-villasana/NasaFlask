# app/__init__.py (Versión final con CORS)

import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS # <-- 1. Importar la nueva librería

load_dotenv()

class Config:
    """Clase de configuración para cargar las variables de entorno."""
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def create_app():
    app = Flask(__name__)

    # --- 2. APLICAR CORS A LA APLICACIÓN ---
    # Esto le dirá a Flask que añada las cabeceras de permiso a todas las respuestas.
    CORS(app) 

    app.config.from_object(Config)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app