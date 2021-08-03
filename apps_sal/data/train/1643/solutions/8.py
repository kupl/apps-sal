try:
    from math import comb
except ImportError:
    from math import factorial

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return factorial(n) // (factorial(k) * factorial(n - k))


def almost_everywhere_zero(n, k):
    digits = list(reversed([int(c) for c in str(n + 1)]))
    aez = 0
    for i in range(len(digits) - 1, -1, -1):
        d = digits[i]
        if d == 0:
            continue
        aez += comb(i, k) * 9**k
        k -= 1
        if k < 0:
            break
        aez += (d - 1) * comb(i, k) * 9**(k)
    return aez
