def smallest_integer(arr):
    res = sorted(set(x for row in arr for x in row))
    for x in range(res[-1]):
        if x not in res:
            return x
    return max(res[-1] + 1, 0)
