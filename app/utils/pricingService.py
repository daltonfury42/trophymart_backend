def get_price(data, config):

    try:
        shape_name = data['shape']
        material_name = data['material']
        coating_name = data['coating']
    except KeyError as ex:
        return {'error': 'param missing: ' + ex.args[0]}

    try:
        shape = config.get('SHAPES')[shape_name]
        material = config.get('MATERIALS')[material_name]
        coating_material = config.get('COATINGS')[coating_name]
    except KeyError as ex:
        return {'error': 'invalid input: ' + ex.args[0]}

    try:
        param_values = [float(data[param]) for param in shape['params']]
    except KeyError as ex:
        return {'error': 'param missing: ' + ex.args[0]}

    volume = shape['volume_func'](*param_values)
    area = shape['volume_func'](*param_values)

    material_price = volume * material['price']
    coating_price = area * coating_material['price']

    price = {
        'material'  : material_price,
        'coating'   : coating_price,
        'total'     : material_price + coating_price
    }

    data['price'] = price

    return data

