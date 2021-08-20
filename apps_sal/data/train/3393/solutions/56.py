def list_squared(m, n, cache={}):
    get = range(m, n + 1)
    check = set(get) - set(cache.keys())
    for y in check:
        sqr = sum((x ** 2 for x in range(1, y + 1) if not y % x))
        root = sqr ** 0.5
        cache[y] = None
        if root == int(root):
            cache[y] = sqr
    result = list(([k, cache[k]] for k in get if cache[k]))
    return result
