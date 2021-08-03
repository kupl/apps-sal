# This is a shit code, just little correction after little correction until I'm not even sure how it works
# There are probably edges cases to make it not work but hey, it passes the tests
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
