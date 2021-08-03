def triangle(x):
    c, r = ["R", "G", "B"], []
    if len(x) == 1:
        return x[0]
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            r.append(x[i])
        else:
            r += [e for e in c if e not in [x[i], x[i + 1]]]
    return triangle(r)
