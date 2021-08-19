def mango(quantity, price):
    (s, e) = divmod(quantity, 3)
    return price * (2 * s + e)
