from itertools import groupby


def radix_tree(*words):
    d = {}
    if not any(words):
        return d
    words = sorted(words)
    for g in (list(g) for (_, g) in groupby(words, key=lambda w: w[0] if w else '')):
        i = next((i for i in range(len(g[0])) if not all((len(w) > i and w[i] == g[0][i] for w in g))), len(g[0]))
        d[g[0][:i]] = radix_tree(*(w[i:] for w in g if len(w) > i))
    return d
