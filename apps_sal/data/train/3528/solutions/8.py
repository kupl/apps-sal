def compound_array(a, b):
    r = []
    for i in [[i, j] for (i, j) in zip(a, b)]:
        r.append(i[0])
        r.append(i[1])
    return r + a[min(len(a), len(b)):] + b[min(len(a), len(b)):]
