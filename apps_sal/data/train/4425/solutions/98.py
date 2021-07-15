def mango(quantity, price):
    a = quantity%3
    b = quantity - a
    c = 2*b/3
    d = c*price + a*price
    return d
