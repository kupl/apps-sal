n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
f = [0 for i in range(n)]
q = [0 for i in range(n)]
d = [int(s) for s in input().split()]

last = d[0]
for i in range(1, n):
    a[i] = a[i - 1]
    if d[i] <= last:
        a[i] += abs(d[i] - last) + 1
        last += 1
    else:
        last = d[i]
    f[i] = last

last = d[n - 1]
for i in range(n - 2, -1, -1):
    b[i] = b[i + 1]
    if d[i] <= last:
        b[i] += abs(d[i] - last) + 1
        last += 1
    else:
        last = d[i]
    q[i] = last

ans = float('inf')
for i in range(n - 1):
    ans = min(ans, a[i] + b[i + 1] + int(f[i] == q[i + 1]))


print(min(ans, b[0], a[n - 1]))
