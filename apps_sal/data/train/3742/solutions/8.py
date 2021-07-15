def modes(data):
    d = {}
    for i in set(data):
        d[data.count(i)] = d.get(data.count(i), []) + [i]
    if len(d) == 1:
        return []
    else:
        return sorted(d[max(d.keys())])
