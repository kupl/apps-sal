from functools import reduce

config = {
    'fib':  ([0, 0, 0, 1], lambda a: a[3] + a[2]),
    'jac':  ([0, 0, 0, 1], lambda a: a[3] + 2 * a[2]),
    'pad':  ([0, 1, 0, 0], lambda a: a[2] + a[1]),
    'pel':  ([0, 0, 0, 1], lambda a: 2 * a[3] + a[2]),
    'tet':  ([0, 0, 0, 1], lambda a: a[3] + a[2] + a[1] + a[0]),
    'tri':  ([0, 0, 0, 1], lambda a: a[3] + a[2] + a[1])
}

def zozonacci(p, l):
    if not p or not l: return []
    return reduce(lambda r, i: r + [config[p[i % len(p)]][1](r[-4:])], range(0, l-4), config[p[0]][0][:])[0:l]
