from itertools import product as p


def proc_seq(*a):
    r, s = [], []
    for i, x in enumerate(map(str, a)):
        s += [''.join(set(d for d in x if d != '0' or i))]
    for x in p(*[[d for d in x] for x in s]):
        r += [int(''.join(x))]
    l, h = min(r), max(r)
    return [len(r)] + ([] if l == h else [l, h]) + [sum(r)]
