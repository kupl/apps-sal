def merge_arrays(first, second):
    a = []
    for i in first:
        if i not in a:
            a.append(i)
    for i in second:
        if i not in a:
            a.append(i)
    a.sort()
    return a
