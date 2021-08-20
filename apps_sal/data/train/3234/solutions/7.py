def select_subarray(arr):
    s = 0
    p = 1
    for x in arr:
        s += x
        p *= x
    result = []
    q = None
    for (i, x) in enumerate(arr):
        if s != x:
            new_q = abs(p / x / (s - x))
            if not result or new_q < q:
                result = [[i, x]]
                q = new_q
            elif new_q == q:
                result.append([i, x])
    return result if len(result) > 1 else result[0]
