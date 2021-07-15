def mango(quantity, price):
    if quantity % 3 == 0:
        return quantity * 2 / 3 * price
    else:
        return (quantity - quantity // 3) * price
