def cycle(sequence):
    d = {}
    for i, x in enumerate(sequence):
        if x in d:
            return [d[x], i - d[x]]
        d[x] = i
    return []
