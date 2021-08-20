import itertools


def de_nico(key, msg):
    pack = [list(range(len(key)))] + list((list(msg[i:i + len(key)]) for i in range(0, len(msg), len(key))))
    sor = [sorted(key).index(i) for i in key]
    sorting = sorted(itertools.zip_longest(*pack, fillvalue=''), key=lambda col: sor.index(col[0]))
    return ''.join([''.join(j) for (i, j) in enumerate(itertools.zip_longest(*sorting, fillvalue=' ')) if i > 0]).strip(' ')
