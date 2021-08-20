def bin2gray(b):
    return [b[0]] + [b[i + 1] ^ j for (i, j) in enumerate(b[:-1])]


def gray2bin(g):
    b = [g[0]]
    for i in g[1:]:
        b.append(b[-1] ^ i)
    return b
