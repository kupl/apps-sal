def nb_dig(n, d):
    thing = 0
    d = str(d)
    num = [str(i**2) for i in range(n + 1)]
    for i in num:
        if d in i:
            thing += i.count(d)
    return thing
