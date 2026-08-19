from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create databse object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.congig['SQLALCHEMY_DATABASE_URL'] = 'sqllite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app)

    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint()
