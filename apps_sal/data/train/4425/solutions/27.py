def mango(quantity, price):
    s, e = divmod(quantity, 3)  # set of three + extra
    return price * ((2 * s) + e)  # 3 for 2 + extra
