def f(c):
    t = s + c
    i = 0
    r = 1
    while i < len(t):
        j = t.rfind(c, i, i + k)
        if j < 0:
            return n
        r += 1
        i = j + 1
    return r


def R():
    return list(map(int, input().split()))


(t,) = R()
for _ in range(t):
    (n, k) = R()
    n += 3
    s = ''.join((f'{x % 2}' for x in R()))
    print(min((f(c) for c in '01')) % n - 1)
