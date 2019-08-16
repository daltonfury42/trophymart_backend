def get_price(shape, material, coating_material, param_values):
    volume = shape['volume_func'](*param_values)
    area = shape['volume_func'](*param_values)

    material_price = volume * material['price']
    coating_price = area * coating_material['price']

    price = {
        'material'  : material_price,
        'coating'   : coating_price,
        'total'     : material_price + coating_price
    }

    return price

