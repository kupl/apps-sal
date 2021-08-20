def triangle(row):
    k = list(row)
    comb = {'R', 'G', 'B'}
    if len(k) == 1:
        return k[0]
    z = [k[i:i + 2] for i in range(len(k) - 1)]
    cont = []
    for x in z:
        diff = comb.difference(set(x))
        if len(diff) == 1:
            cont.append(diff.pop())
        else:
            cont.append(x[0])
    return triangle(''.join(cont))
