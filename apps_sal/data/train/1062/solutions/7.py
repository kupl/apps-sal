n = int(input())
k = n
m = 0
t = 0
d = 2 * n - 2
for i in range(n):
    l = i + 1
    k = n
    for j in range(i + 1):
        print(k, end=' ')
        k -= 1
    g = d - m
    while g - t > 0:
        print(k + 1, end=' ')
        g -= 1
    h = m
    k += 2
    while h > 0:
        print(k, end=' ')
        h -= 1
        k += 1
    m += 1
    t += 1
    print()
k = n - 1
t = 1
m -= 1
for i in range(n - 1):
    l = k - i
    d = k + 1
    for j in range(l, 0, -1):
        print(d, end=' ')
        d -= 1
    f = t
    while f > 0:
        print(d + 1, end=' ')
        f -= 1
    b = d + 1
    v = m
    while v > 0:
        print(b, end=' ')
        v -= 1
        b += 1
    t += 2
    m -= 1
    print()
