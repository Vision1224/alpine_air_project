from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['TEMPLATES_AUTO_RELOAD'] = True

    from .views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
