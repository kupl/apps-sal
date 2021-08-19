t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    l = []
    count = 0
    for i in range(n):
        (a, b) = input().split()
        l.append(a)
        if (a, b) not in d:
            d[a, b] = 0
        d[a, b] += 1
    l = set(l)
    for i in l:
        count += d.get((i, '0'), 0) if d.get((i, '0'), 0) > d.get((i, '1'), 0) else d.get((i, '1'), 0)
    print(count)
