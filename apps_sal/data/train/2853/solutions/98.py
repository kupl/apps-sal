def solve(arr):
    ret = []
    for el in list(reversed(arr)):
        if el not in ret:
            ret.append(el)
    return list(reversed(ret))
