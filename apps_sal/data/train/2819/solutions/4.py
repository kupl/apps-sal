from functools import wraps


def cache(f):
    _cache = {}

    @wraps(f)
    def wrapped(n):
        if n in _cache:
            return _cache[n]
        else:
            result = f(n)
            _cache[n] = result
            return result
    return wrapped


@cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
