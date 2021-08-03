def mango(quantity, price):

    free = quantity // 3
    res = (quantity - free) * price
    return res
