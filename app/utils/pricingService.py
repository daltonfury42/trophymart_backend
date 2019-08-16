def get_price(data, config):

    shape = config.get('SHAPES')[data['shape']]

    try:
        param_values = [float(data[param]) for param in shape['params']]
    except KeyError as ex:
        return {'error': 'param missing: ' + ex.args[0]}

    return shape['volume_func'](*param_values)
