n = int(input())
a = list(map(int, input().split()))
q = int(input())
r1 = [-1] * q
r2 = [-1] * q
for i in range(q):
    ne = list(map(int, input().split()))
    if ne[0] == 1:
        p = ne[1] - 1
        t = ne[2]
        r1[i] = [p, t]
    else:
        r2[i] = ne[1]

b = -1
for i in range(q - 1, -1, -1):
    b = max(b, r2[i])
    r2[i] = b

m = r2[0]
for i in range(n):
    a[i] = max(a[i], m)

for i in range(q):
    if r1[i] == -1:
        pass
    else:
        a[r1[i][0]] = max(r1[i][1], r2[i])

print(*a)
