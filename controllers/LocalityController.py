from flask import Blueprint, jsonify
# from flask_restx import Namespace, Resource, fields

from services.LocalityService import LocalityService

# api = Namespace("api", description="Localities with postal codes")

# locality = api.model(
#     name="Locality",
#     model={
#         "key": fields.String(required=True, description="Postal code, 5 numbers length"),
#         "name": fields.String(required=True, description="Name of locality")
#     }
# )

# @api.route('/localities/<cp>')

class LocalityController:

    service = LocalityService()
    blueprint = None
    root = '/api/localities'
    def __init__(self) -> None:
        self.blueprint = Blueprint("Localities", __name__)
        self.blueprint.add_url_rule(self.root + '/<cp>', self.root + '/<cp>/get' ,self.get, methods = ['GET'])
        pass
    # @api.route('/<cp>')
    # @api.marshal_with(locality)
    # @api.param("cp", "Postal code")
    # @api.response(200, "List of localities")
    def get(self, cp: int):
        response = self.service.getLocality(cp)
        lst = [o.__dict__ for o in response]
        return jsonify({'entities':lst})