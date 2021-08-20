M = {'^': -1, 'v': 1, '<': -1j, '>': 1j}


def rem(D, k):
    del D[k]


def simplify(path):
    (D, z, res) = ({0: 0}, 0, list(path))
    for (i, c) in enumerate(path, 1):
        z += M[c]
        if z in D:
            for j in range(D[z], i):
                res[j] = None
            [rem(D, k) for (k, v) in list(D.items()) if v > D[z]]
        else:
            D[z] = i
    return ''.join(filter(None, res))
