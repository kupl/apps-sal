def modes(data):
    d = {i: data.count(i) for i in set(data)}
    return [] if len(set(d.values())) == 1 else sorted([i for i in set(data) if d[i] == max(d.values())])
