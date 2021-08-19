# https://oeis.org/A203464
from bisect import bisect
s = [0]
for m in range(0, 10**9):
    for p in (4, 9, 56, 61):
        s.append(s[-1] + m * 65 + p)
    if s[-1] > 52 * 10**13:
        break


def find_closest_value(m):
    if m < 4:
        return 4
    i = bisect(s, m)
    return s[min([i, i - 1], key=lambda i:abs(s[i] - m))]
