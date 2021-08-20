from collections import defaultdict


def group_cities(seq):

    def key(s):
        return min((s[i:] + s[:i] for i in range(len(s))))
    d = defaultdict(set)
    for e in seq:
        d[key(e.lower())].add(e)
    return sorted((sorted(v) for v in d.values()), key=lambda x: (-len(x), x))
