n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = [b[0]]
p1 = [a[0]]
p2 = [a[0] - b[0]]
for i in range(1, n):
    p.append(b[i] + p[i - 1])
for i in range(1, n):
    p1.append(max(p1[i - 1], a[i] + p[i - 1]))
for i in range(1, n):
    p2.append(max(p2[i - 1], a[i] - p[i]))
maxi = max(a)
for i in range(1, n):
    maxi = max(maxi, a[i] + p[i - 1] + p2[i - 1])
    maxi = max(maxi, p[n - 1] + a[i] - p[i] + p1[i - 1])
print(maxi)
