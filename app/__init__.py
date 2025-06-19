from flask import Flask

def create_app():
    app = Flask(__name__)

    from .ghostlog import ghostlog_bp
    from .reflex_score import reflex_bp
    from .webhook import webhook_bp
    app.register_blueprint(ghostlog_bp, url_prefix='/api')
    app.register_blueprint(reflex_bp, url_prefix='/api')
    app.register_blueprint(webhook_bp, url_prefix='/api')

    return app
