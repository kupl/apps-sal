from functools import cmp_to_key


def f(s, t):
    m = min(len(s), len(t))
    if s[:m] > t[:m]:
        return 1
    elif s[:m] < t[:m]:
        return -1
    elif len(s) > len(t):
        return -1
    else:
        return 1


def ms(s, t):
    i = 0
    for (c1, c2) in zip(s, t):
        if c1 != c2:
            return i
        i += 1
    return i


def xxor(x):
    if x & 3 == 0:
        return x
    if x & 3 == 1:
        return 1
    if x & 3 == 2:
        return x + 1
    if x & 3 == 3:
        return 0


def gray(x):
    return x ^ x // 2


(n, l) = list(map(int, input().split()))
s = [input() for _ in range(n)]
s.sort(key=cmp_to_key(f))
g = gray(l) ^ gray(l - len(s[0]))
for i in range(n - 1):
    b = ms(s[i], s[i + 1]) + 1
    g ^= gray(l - b + 1) ^ gray(l - b)
    t = len(s[i + 1]) - b
    g ^= gray(l - b) ^ gray(l - b - t)
if g == 0:
    print('Bob')
else:
    print('Alice')
