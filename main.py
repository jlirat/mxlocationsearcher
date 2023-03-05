from flask import Flask
from flask_restx import Api
from controllers.LocalityController import LocalityController
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from doc import api
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

app.register_blueprint(LocalityController().blueprint)
@app.route("/")

def hello_world():
    return "<p>Online</p>"