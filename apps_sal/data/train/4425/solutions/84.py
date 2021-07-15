def mango(quantity, price):
    ost = quantity % 3
    return ((quantity-ost) * 2 / 3 + ost) * price
