from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Global db instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')

    # app.config['UPLOAD_FOLDER'] = os.path.join('app', 'static', 'uploads')
    # app.config['AUDIO_FOLDER'] = os.path.join('app', 'static', 'audio')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/ocr_data.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
