from flask import Flask
from flask_caching import Cache

cache = Cache()
def create_app():
    app = Flask(__name__)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    from .main import main as main_blueprint
    # Register the blueprint
    app.register_blueprint(main_blueprint)
    
    return app
