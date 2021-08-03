def merge_arrays(first, second):
    working = []
    for e in first:
        if e not in working:
            working.append(e)
    for i in second:
        if i not in working:
            working.append(i)
    return sorted(working)
