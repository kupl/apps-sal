import sys
sys.setrecursionlimit(10000)


def combs_non_empty_boxes(n, k):
    if k > n:
        return 'It cannot be possible!'

    return stirling(n, k)


def memoize(f):
    memo = {}

    def wrapping(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return wrapping


@memoize
def stirling(n, k):
    if n == 0 and k == 0:
        return 1

    if n == 0 or k == 0:
        return 0

    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)
