r = N = 1 << int(input())
d = [[int(s)] for s in input().split()]
while r > 1:
    r >>= 1
    for i in range(N):
        if i & r:
            d[i] = sorted(d[i ^ r] + d[i])[-2:]
for (a, b) in d[1:]:
    r = max(r, a + b)
    print(r)
