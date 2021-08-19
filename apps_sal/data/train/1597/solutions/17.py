t = int(input())
for _ in range(t):
    d = []
    jj = 0
    (a, m) = list(map(int, input().split()))
    p = m // (a + 1)
    q = m // a
    for i in range(p, q + 1):
        if i != m / a:
            if i % (m - a * i) == 0:
                d.append(i)
    print(len(d))
    d.sort()
    for u in d:
        print(u, end=' ')
    print('\n', end='')
