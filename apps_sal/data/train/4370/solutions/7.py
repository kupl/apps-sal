def indices(n, d):
    if n == 1:
        return [[d]]
    result = []
    for i in range(d + 1):
        for x in indices(n - 1, d - i):
            result.append([i] + x)
    return result
