def array_madness(a,b):
    for i in range(len(a)):
        a[i] = a[i]**2
    suma= sum(a)
    for i in range(len(b)):
        b[i] = b[i]**3
    sumb = sum(b)
    if suma > sumb:
        return True
    else:
        return False
    # Ready, get, set, GO!!!

