def sale_hotdogs(n):

    fiyat = 0

    if n < 5:
        fiyat = 100
    elif n >= 5 and n < 10:
        fiyat = 95
    elif n >= 10:
        fiyat = 90

    return n * fiyat
