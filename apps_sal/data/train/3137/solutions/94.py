def round_it(n):
    import math
    point = str(n).index('.')
    mayor = str(n)[0:point]
    menor = str(n)[point + 1:]
    if len(mayor) > len(menor):
        return math.floor(n)
    elif len(mayor) < len(menor):
        return math.ceil(n)
    elif len(mayor) == len(menor):
        return round(n)
