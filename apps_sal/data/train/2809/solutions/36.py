def digitize(n):
    lista = str(n)
    listan = list(lista)
    listan.reverse()
    for i in range(0, len(listan)):
        listan[i] = int(listan[i])
    return listan
