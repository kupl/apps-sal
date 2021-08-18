t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(n):
        l[i] = l[i] % p
    d = {}
    for i in range(n):
        c = 0
        for j in range(i, n):
            c += l[j]
            try:
                d[c % p] += 1
            except:
                d[c % p] = 1
    x = max(list(d.keys()))
    print(x, d[x])
