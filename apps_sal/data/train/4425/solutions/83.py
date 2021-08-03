def mango(quantity, price):
    p2 = price * 2
    calc = divmod(quantity, 3)

    calc2 = calc[0] * p2
    return calc2 + (calc[1] * price)
