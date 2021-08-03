def merge_arrays(first, second):
    res = []
    [res.append(x) for x in first + second if x not in res]
    return sorted(res)
