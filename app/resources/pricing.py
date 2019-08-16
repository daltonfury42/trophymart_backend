from flask import Blueprint, request, current_app, jsonify

from app.services import pricingService
from app.utils.errors import InvalidUsage, Errors

pricing = Blueprint('pricing', __name__, url_prefix='/pricing')


@pricing.route('/')
def get_pricing():
    data = request.json
    config = current_app.config

    try:
        shape_name = data['shape']
        material_name = data['material']
        coating_name = data['coating']
    except KeyError as ex:
        raise InvalidUsage(Errors.PARAM_NOT_FOUND, {'error_param': ex.args[0]})

    try:
        shape = config.get('SHAPES')[shape_name]
        material = config.get('MATERIALS')[material_name]
        coating_material = config.get('COATINGS')[coating_name]
    except KeyError as ex:
        raise InvalidUsage(Errors.INVALID_PARAM, {'error_input': ex.args[0]})

    try:
        dimension_values = [float(data['dimensions'][dimension]) for dimension in shape['dimensions']]
    except KeyError as ex:
        raise InvalidUsage(Errors.PARAM_NOT_FOUND, {'error_dimension': ex.args[0]})

    price = pricingService.get_price(shape, material, coating_material, dimension_values)

    data['price'] = price

    return jsonify(data)


@pricing.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response