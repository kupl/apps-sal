from functools import lru_cache


@lru_cache(maxsize=None)
def calc(d, k, is_first_digit=True):
    if d < 0 or k < 0 or d < k:
        return 0
    elif d == k:
        return 9 ** k
    return calc(d - 1, k - 1, False) * 9 + calc(d - 1, k, False) * (not is_first_digit)


def almost_everywhere_zero(n, k):
    if n < 10:
        return {0: 1, 1: n}.get(k, 0)
    ans = sum(calc(d, k) for d in range(k, len(str(n))))
    for d in range(1, int(str(n)[0])):
        ans += calc(len(str(n)) - 1, k - 1, False)
    return ans + almost_everywhere_zero(int(str(n)[1:]), k - 1)
