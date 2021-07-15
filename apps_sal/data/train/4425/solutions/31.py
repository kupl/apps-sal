def mango(quantity, price):
    return 2 * price if quantity == 3 else (quantity - (quantity // 3)) * price

