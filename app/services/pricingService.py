def get_price(shape, material, coating_material, dimension_values):
    volume = shape['volume_func'](*dimension_values)
    area = shape['volume_func'](*dimension_values)

    material_price = volume * material['price']
    coating_price = area * coating_material['price']

    price = {
        'material'  : material_price,
        'coating'   : coating_price,
        'total'     : material_price + coating_price
    }

    return price

