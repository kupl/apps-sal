N, d, r = int(input()), [], 0
for a in map(int, input().split()):
    d.append([-a])
for n in range(N):
    B = 1 << n
    for i in range(1 << N):
        if i & B:
            d[i] = sorted(d[i ^ B] + d[i])[:2]
for a, b in d[1:]:
    r = min(r, a + b)
    print(-r)
