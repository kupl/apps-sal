def mango(quantity, price):
    result = divmod(quantity,3)
    return result[0]*2*price + result[1] * price
