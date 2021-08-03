def merge_arrays(first, second):
    first = first + second
    res = []
    for i in first:
        if i not in res:
            res.append(i)
    return sorted(res)
