def row_weights(l):
    s = [0, 0]
    for i in range(len(l)):
        if i % 2 == 0:
            s[0] += l[i]
        else:
            s[1] += l[i]
    return tuple(s)
