n, m, k = map(int, input().split())
c = 0
for i in range(n):
    t = list(map(int, input().split()))
    if t[-1] <= 10 and sum(t) - t[-1] >= m:
        c += 1
print(c)
