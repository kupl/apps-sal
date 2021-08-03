acci = {
    "fib": ([0, 0, 0, 1], [-1, -2]),
    "jac": ([0, 0, 0, 1], [-1, -2, -2]),
    "pad": ([0, 1, 0, 0], [-2, -3]),
    "pel": ([0, 0, 0, 1], [-1, -1, -2]),
    "tet": ([0, 0, 0, 1], [-1, -2, -3, -4]),
    "tri": ([0, 0, 0, 1], [-1, -2, -3])
}


def zozonacci(p, l):
    if not p:
        return []
    h, i = acci[p[0]][0][:], 0
    while len(h) < l:
        h.append(sum(h[j] for j in acci[p[i]][1]))
        i = (i + 1) % len(p)
    return h[:l]
