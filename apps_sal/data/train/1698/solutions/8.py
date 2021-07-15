def dbl_linear(n):
    x = 1
    ys = []
    zs = []

    for i in range(n):
        ys.append(2*x + 1)
        zs.append(3*x + 1)
        miny = ys[0]
        minz = zs[0]
        x = miny if miny < minz else minz
        if x == miny: ys.pop(0)
        if x == minz: zs.pop(0)

    return x

