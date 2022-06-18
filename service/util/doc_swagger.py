from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'a': fields.Float(required=True, description="Coeficiente A da equação"),
    'b': fields.Float(required=True, description="Coeficiente B da equação"),
    'c': fields.Float(required=True, description="Coeficiente C da equação")})
