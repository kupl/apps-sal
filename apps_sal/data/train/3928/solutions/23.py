def billboard(name, price=30):
    suma=0
    s=len(name)
    for i in range(1, s+1):
        suma+=price
    return suma
