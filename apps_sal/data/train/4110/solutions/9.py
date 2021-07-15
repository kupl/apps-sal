def matrixfy(st):
    import math
    if len(st) == 0:
        return "name must be at least one letter"
    a = math.ceil(len(st) ** 0.5)
    b = []
    for i in range(a):
        b.append(list(a * "."))
    for j in range(a):
        for k in range(a):
            if j * a + k == len(st):
                return b
            else:
                b[j][k] = st[j * a + k]
    return b
