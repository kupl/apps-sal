def array_madness(a,b):
    suma=0
    sumb=0
    for i in a:
        suma += i ** 2
    for j in b:
        sumb += j ** 3
    return True if suma > sumb else False
        

