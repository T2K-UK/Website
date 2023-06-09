from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "allinfo.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'THE SECRETEST OF KEYS'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Booking

    with app.app_context():
        if not path.exists('website/website/' + DB_NAME):
            db.create_all()
            print('Created database!')
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))

    return app



