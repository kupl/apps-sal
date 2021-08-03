def group_cities(seq):
    res = {}
    for w in seq:
        temp = [str(w[i:] + w[:i]).title() for i in range(1, len(w))
                if str(w[i:] + w[:i]).title() in seq]
        temp.append(w)
        res[frozenset(temp)] = sorted(set(temp))
    return sorted(res.values(), key=lambda x: (-len(x), x[0]))
