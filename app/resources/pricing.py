from flask import Blueprint, request, current_app, jsonify

from app.utils import pricingService
from app.utils.errors import InvalidUsage

pricing = Blueprint('pricing', __name__, url_prefix='/pricing')


@pricing.route('/')
def get_pricing():
    data = request.json

    return jsonify(pricingService.get_price(data, current_app.config))


@pricing.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response