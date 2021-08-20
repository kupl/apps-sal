def memoize(func):
    cache = {}

    def decorator(x):
        if not x in cache:
            cache[x] = func(x)
        return cache[x]
    return decorator


@memoize
def permutations(d):
    if d < 1:
        return []
    if d == 1:
        return ['0']
    return sorted((p[:i] + str(d - 1) + p[i:] for p in permutations(d - 1) for i in range(d)))


def nth_perm(n, d):
    return permutations(d)[n - 1]
