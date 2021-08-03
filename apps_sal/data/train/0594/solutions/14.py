n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
i = 0
x = sum(l)
d = x
m = 0
for i in range(n):
    c = 0
    for j in range(i, n):
        c += l[j]
        m = max(c, m)
d -= m
d += m / k


print(d)
