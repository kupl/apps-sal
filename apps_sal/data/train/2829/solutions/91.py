def array_madness(a, b):
    Listea = list()
    Listeb = list()
    for ch in a:
        Listea.append(ch ** 2)
        suma = sum(Listea)
    for ch in b:
        Listeb.append(ch ** 3)
        sumb = sum(Listeb)
    if suma > sumb:
        return True
    else:
        return False
