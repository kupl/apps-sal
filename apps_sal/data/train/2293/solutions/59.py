(N, r, d) = (1 << int(input()), 0, [[int(s)] for s in input().split()])
B = 1
while B < N:
    for i in range(N):
        if i & B:
            d[i] = sorted(d[i ^ B] + d[i])[-2:]
    B <<= 1
for (a, b) in d[1:]:
    r = max(r, a + b)
    print(r)
