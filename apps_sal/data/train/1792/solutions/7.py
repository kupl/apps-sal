cache_f = {}
cache_g = {}


def f(n):
    if n in cache_f:
        return cache_f[n]
    if n == 0:
        return 1
    if n == 1:
        return 0
    else:

        def g(n):
            if n in cache_g:
                return cache_g[n]
            if n == 0:
                cache_g[0] = 0
                return 0
            if n == 1:
                cache_g[1] = 1
                return 1
            else:
                cache_g[n] = f(n - 1) + g(n - 2)
                return f(n - 1) + g(n - 2)
        cache_f[n] = f(n - 2) + 2 * g(n - 1)
        return f(n - 2) + 2 * g(n - 1)


for i in range(1, 11):
    f(998 * i)


def three_by_n(n):
    if n % 2 == 0:
        return f(n) % 12345787
    else:
        res = 0
        for i in range((n - 1) // 2):
            res += cache_g[n - 2 * (i + 1)] * cache_g[2 * i + 1] * 2
        res += (n + 1) * cache_g[n]
        return res % 12345787
