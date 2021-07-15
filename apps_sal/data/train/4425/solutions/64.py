def mango(q,p):
    price = 0
    while q % 3 != 0:
        price += p
        q -= 1
    return price+q*(2/3)*p
