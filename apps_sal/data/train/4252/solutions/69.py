def merge_arrays(first, second):
    first.extend(second)
    res = list(set(first))
    res.sort()
    return res
