def rec(arr):
    type = [isinstance(x, int) for x in arr]
    if len(set(type)) > 1:
        return None
    if not type or type[0]:
        return []
    size = list(map(len, arr))
    if len(set(size)) != 1:
        return None
    res = [rec(x) for x in arr]
    if None in res:
        return None
    if len(set(map(tuple, res))) != 1:
        return None
    return [size[0]] + res[0]


def hyperrectangularity_properties(arr):
    res = rec(arr)
    if res is None:
        return None
    return tuple([len(arr)] + res)
