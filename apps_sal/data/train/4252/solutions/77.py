def merge_arrays(first, second):
    c = []
    for x in first:
        c.append(x)
    for x in second:
        c.append(x)
    return sorted(set(c))
