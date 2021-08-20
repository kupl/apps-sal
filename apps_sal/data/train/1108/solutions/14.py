(n, m, k) = map(int, input().split())
c = 0
for i in range(n):
    l = list(map(int, input().split()))
    r = l[:k]
    if sum(r) >= m and l[-1] <= 10:
        c += 1
print(c)
