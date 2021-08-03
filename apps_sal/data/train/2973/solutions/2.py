def array_conversion(l):
    iter = 0
    while len(l) > 1:
        iter += 1
        l = [[l[i] * l[i + 1], l[i] + l[i + 1]][iter % 2] for i in range(0, len(l) - 1, 2)]
    return l[0]
