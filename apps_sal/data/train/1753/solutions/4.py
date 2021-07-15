def memoize(f):
    memo = {}
    def memoized(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return memoized
    
def least_bribes(xs):
    @memoize
    def f(i, j):
        return i - j and min(max(f(i, k), f(k + 1, j)) + xs[k] for k in range(i, j))
    return f(0, len(xs))
