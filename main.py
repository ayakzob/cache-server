from app.cache_api import cache_api
from flask import Flask
from flask_restplus import Api

# main service
app = Flask(__name__)
app.config["ERROR_404_HELP"] = False

# cache endpoint
api = Api(app, prefix="/v1")
api.add_namespace(cache_api, path="/cache")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
