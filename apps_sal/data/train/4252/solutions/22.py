def merge_arrays(first, second):
    l = []
    for n in first:
        if n not in l:
            l.append(n)
    for n in second:
        if n not in l:
            l.append(n)
    return sorted(l)
