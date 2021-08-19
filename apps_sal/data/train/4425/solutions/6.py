def mango(quantity, price):
    (a, b) = divmod(quantity, 3)
    return price * (a * 2 + b)
