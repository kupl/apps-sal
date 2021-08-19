from math import factorial


def nth_permutation(s, n):
    if not s:
        return ''
    m = factorial(len(s) - 1)
    (q, r) = divmod(n, m)
    return s[q] + nth_permutation(s[:q] + s[q + 1:], r)


def middle_permutation(s):
    return nth_permutation(sorted(s), factorial(len(s)) // 2 - 1)
