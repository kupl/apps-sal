n = int(input())
t = [0, 0] + list(map(int, input().split()))
a, b = [0] * (n + 1), [0] * (n + 1)
a[1] = b[1] = -1


def f(s, a, b, l):
    nonlocal t
    l.reverse()
    j, n = 0, len(l)
    while True:
        s += t[l[j]]
        a[l[j]] = s
        j += 1
        if j == n:
            return
        s += t[l[j]]
        b[l[j]] = s
        j += 1
        if j == n:
            return


def g(i, k):
    nonlocal a, b
    l = []
    if k:
        a[i] = -1
        l.append(i)
        i += t[i]
    while True:
        if i > n:
            return f(0, a, b, l)
        if b[i] > 0:
            return f(b[i], a, b, l)
        if b[i] == -1:
            return
        b[i] = -1
        l.append(i)
        i -= t[i]
        if i < 1:
            return f(0, b, a, l)
        if a[i] > 0:
            return f(a[i], b, a, l)
        if a[i] == -1:
            return
        a[i] = -1
        l.append(i)
        i += t[i]


for i in range(2, n + 1):
    if a[i] == 0:
        g(i, True)
    if b[i] == 0:
        g(i, False)

for i in range(1, n):
    if b[i + 1] > 0:
        t[i] = i + b[i + 1]
    else:
        t[i] = -1

print('\n'.join(map(str, t[1: n])))
