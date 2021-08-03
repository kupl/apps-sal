def mango(quantity, price):
    if quantity % 3 == 0:
        return quantity * 2 / 3 * price
    elif quantity % 3 == 1:
        return (quantity - 1) * 2 / 3 * price + price
    elif quantity % 3 == 2:
        return (quantity - 2) * 2 / 3 * price + 2 * price
