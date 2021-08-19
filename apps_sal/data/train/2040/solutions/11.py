from math import hypot
(n, h) = list(map(int, input().split()))
square = 0.5 * h
one = square / n
hyp = hypot(0.5, h)


def get_square(d):
    up = (1 - d) * 0.5
    return 2 * (up * h * d + (0.5 - up) * h * d / 2)


rez = []
_prev = 0
for i in range(n - 1):
    left = _prev
    right = 1
    for i in range(50):
        mid = (left + right) / 2
        if get_square(mid) - get_square(_prev) > one:
            right = mid
        else:
            left = mid
    _prev = left
    rez.append(h - left * h)
print(*reversed(rez))
