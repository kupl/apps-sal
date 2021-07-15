def mango(quantity, price):
    if quantity % 3 == 0:
        return (quantity * 2 * price // 3)
    else:
        return (quantity // 3 * 2 * price + quantity % 3 * price)
