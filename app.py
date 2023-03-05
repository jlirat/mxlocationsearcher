from flask import Flask
from flask_restx import Api
from controllers.LocalityController import LocalityController
# from flask_restx import Api, Resource, fields
# from werkzeug.middleware.proxy_fix import ProxyFix
# from doc import api
app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)

# api.init_app(app)

app.register_blueprint(LocalityController().blueprint)
@app.route("/")
def hello_world():
    return "<p>Online</p>"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)
# [END gae_python37_app]
