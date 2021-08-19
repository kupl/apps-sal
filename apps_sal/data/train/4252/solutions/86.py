def merge_arrays(first, second):
    a = first + second
    res = []
    for x in a:
        if x not in res:
            res.append(x)
    return sorted(res)
