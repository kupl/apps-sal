from collections import Counter
from string import ascii_lowercase as asc
(m, s) = (int(input()), input())
g = Counter(s)


def solve(c):
    p = 0
    for q in ''.join((x if x >= c else ' ' for x in s)).split():
        (i, j) = (0, -1)
        while j + m < len(q):
            j = q.rfind(c, j + 1, j + m + 1)
            if j == -1:
                return None
            i += 1
        p += i
    return p


for c in asc:
    f = solve(c)
    if f is not None:
        g[c] = f
        print(''.join((x * g[x] for x in asc if x <= c)))
        break
