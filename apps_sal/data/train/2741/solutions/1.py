def russian_peasant_multiplication(x, y, product=0):
    product += x if y % 2 else 0
    x += x
    y //= 2
    if y:
        product = russian_peasant_multiplication(x, y, product)
    return product
