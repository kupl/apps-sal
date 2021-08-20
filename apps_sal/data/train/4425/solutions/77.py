def mango(quantity, price):
    return quantity % 3 * price + int(quantity - quantity % 3) / 3 * 2 * price
