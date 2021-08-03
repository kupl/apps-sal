def fibonacci(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
    return n
