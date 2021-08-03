from collections import Counter, defaultdict


def group_cities(seq):
    bases = defaultdict(lambda: defaultdict(list))
    for W in set(seq):
        w = W.lower()
        d = bases[frozenset(Counter(w).items())]
        k = next((w2 for w2 in d if w in w2), w * 2)
        d[k].append(W)

    return sorted([sorted(lst) for d in bases.values() for lst in d.values()],
                  key=lambda g: (-len(g), g[0]))
