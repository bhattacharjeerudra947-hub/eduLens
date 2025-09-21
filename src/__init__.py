import os
from flask import Flask
from src.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):

    DB_USER = "root"
    DB_PASSWORD = "newpassword"
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_NAME = "student_data"

    engine = create_engine(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}")
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
        print(f"Database `{DB_NAME}` is ready.")

    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    login_manager.init_app(app=app)
    db.init_app(app=app)
    bcrypt.init_app(app=app)

    from src.main.routes import main
    from src.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)
    
    return app
