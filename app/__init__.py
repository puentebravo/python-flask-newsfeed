from flask import Flask
from app.routes import home, dashboard
from app.db import init_db

def create_app(test_config=None):
    #This sets up application configuration
    app = Flask(__name__, static_url_path="/")
    app.url_map.strict_slashes= False
    app.config.from_mapping(
        SECRET_KEY= "thisistheway"
    )
    @app.route("/hello")
    def hello():
        return "Is this thing on?"
    
    #This registers routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    init_db()

    return app