from flask import Blueprint, request, current_app, jsonify

from app.utils import pricingService

pricing = Blueprint('pricing', __name__, url_prefix='/pricing')


@pricing.route('/')
def get_pricing():
    data = request.json

    return jsonify(pricingService.get_price(data, current_app.config))


