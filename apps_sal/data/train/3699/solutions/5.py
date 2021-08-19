from collections import Counter


def ranks(a):
    (id, res) = (1, {})
    for (k, v) in sorted(Counter(a).items(), reverse=True):
        (id, res[k]) = (id + v, id)
    return list(map(res.get, a))
