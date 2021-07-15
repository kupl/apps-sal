from itertools import groupby

def replace(stg):
    g = ["".join(s) for _, s in groupby(stg)]
    l = len(g)
    for i in range(l):
        for j in range(i+1, l, 2):
            if " " not in f"{g[i]}{g[j]}" and len(g[i]) == len(g[j]):
                g[i] = g[j] = " " * len(g[i])
    return "".join(g)
