def memoize(f):
    memo = {}
    def memoized(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return memoized
    
def least_bribes(bribes):

    @memoize
    def f(i, j):
        assert i <= j
        if i == j: return 0
        if i + 1 == j: return bribes[i]
        return min(max(f(i, k),f(k + 1, j)) + bribes[k] for k in xrange(i, j))

    return f(0, len(bribes))
