n, k = map(int, input().split())
hs = sorted([int(input()) for _ in range(n)])
m = hs[k - 1] - hs[0]
i = k
while i < n:
    new = hs[i] - hs[i - k + 1]
    if new < m:
        m = new
    i += 1
print(m)
