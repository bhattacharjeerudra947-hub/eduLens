from flask import Flask
from src.config import Config

def create_app(config_class=Config):

    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    from src.main.routes import main

    app.register_blueprint(main)
    
    return app
