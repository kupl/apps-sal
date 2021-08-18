def array_madness(a, b):
    suma = 0
    sumb = 0
    for i in a:
        suma += i * i
    for i in b:
        sumb += i * i * i
    return suma > sumb
