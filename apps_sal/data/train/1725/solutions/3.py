dp = {}


def circular_limited_sums(max_n, max_fn):
    if max_n == 1:
        return (max_fn // 2) + 1
    else:
        s = 0
        for i in range(max_fn + 1):
            s += solve(max_n - 1, max_fn, i, i)
            s %= 12345787
        return s


def solve(n, m, first, last):

    if (n, m, first, last) in dp:
        return dp[(n, m, first, last)]

    if n == 1:
        dp[(n, m, first, last)] = m - max(first, last) + 1
        return dp[(n, m, first, last)]

    s = 0
    for i in range(m - last + 1):
        if first is None:
            s += solve(n - 1, m, i, i)
        else:
            s += solve(n - 1, m, first, i)
        s %= 12345787

    dp[(n, m, first, last)] = s
    return dp[(n, m, first, last)]
