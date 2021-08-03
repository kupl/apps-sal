def find_multiples(integer, limit):
    k = list()
    if limit < integer:
        return k
    for a in range(1, limit // integer + 1):
        k.append(a * integer)
    return k
