def mango(quantity, price):
    q,r = divmod(quantity,3)
    return price*(2*q+r)
