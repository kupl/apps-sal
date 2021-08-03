from collections import Counter


def factorize(n):
    f = []
    for i in range(2, n + 1):
        while n % i == 0:
            f.append(i)
            n /= i
    return Counter(f)


def zeroes(base, number):
    f, l = factorize(base), []
    for factor in f:
        ans, n = 0, number
        while n >= factor:
            ans += n // factor
            n = n // factor
        ans = ans // f[factor]
        l.append(ans)
    return min(l)
