import itertools


def connect_four_place(columns):
    cs = [[] for i in range(7)]
    for (color, i) in zip(itertools.cycle('YR'), columns):
        cs[i].append(color)
    for c in cs:
        c.extend(['-'] * (6 - len(c)))
    return [list(x) for x in zip(*cs)][::-1]
