def automorphic(n):
    kvad = n ** 2
    m = []
    stroki = str(n)
    stroka = str(kvad)
    mass = list(stroka)
    leni = len(stroka)
    leni2 = len(stroki)
    mass = list(reversed(mass))
    while leni != leni2:
        leni = leni - 1
        mass.pop()
    mass = list(reversed(mass))
    b = str(n)
    b = list(b)
    if b == mass:
        return 'Automorphic'
    else:
        return 'Not!!'
