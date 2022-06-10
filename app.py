from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.config.from_prefixed_env()

    print(app.config["SECRET_KEY"])

    return app