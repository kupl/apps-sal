from math import ceil


def distance(n):
    border = ceil(int(n ** .5) / 2) + int(not (n ** .5).is_integer())
    k = border * 2 - 1
    a = k ** 2
    for i in range(4):
        if a - k < n <= a:
            return (border - 1) + abs(n - ((a - k + 1) + a) // 2)
        a -= (k - 1)
