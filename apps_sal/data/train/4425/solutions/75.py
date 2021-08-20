def mango(quantity, price):
    q = quantity // 3 * 2
    q += quantity - q * 1.5
    return q * price
