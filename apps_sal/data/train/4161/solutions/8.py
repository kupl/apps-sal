def rat_at(n):
    if n == 0:
        return (1, 1)
    for l in range(1001):
        if 2 ** l - 1 <= n <= 2 ** (l + 1) - 2:
            i = l
            break
    if n % 2 == 1:
        j = int((n - (2 ** i - 1)) / 2 + 2 ** (i - 1) - 1)
        k = rat_at(j)
        return (k[0], k[0] + k[1])
    else:
        j = int((n - (2 ** i)) / 2 + 2 ** (i - 1) - 1)
        k = rat_at(j)
        return (k[0] + k[1], k[1])


def index_of(a, b):
    if (a, b) == (1, 1):
        return 0
    if a > b:
        n = index_of(a - b, b)
        k = n
        for l in range(1001):
            if 2 ** l - 1 <= n <= 2 ** (l + 1) - 2:
                i = l
                break
        return k + ((k - (2 ** i - 1)) * 2 + 1 + (2 ** (i + 1) - 1 - k))
    else:
        n = index_of(a, b - a)
        k = n
        for l in range(1001):
            if 2 ** l - 1 <= n <= 2 ** (l + 1) - 2:
                i = l
                break
        return k + ((k - (2 ** i - 1)) * 2 + 1 + (2 ** (i + 1) - 1 - k)) - 1
