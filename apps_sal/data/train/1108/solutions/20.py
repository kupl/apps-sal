(n, m, k) = map(int, input().split())
c = 0
for i in range(n):
    l = list(map(int, input().split()))
    s = sum(l) - l[-1]
    if s >= m and l[-1] <= 10:
        c += 1
print(c)
