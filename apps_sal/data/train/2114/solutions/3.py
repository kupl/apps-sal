a = input().split(' ')
n = int(a[0])
m = int(a[1])
b = input().split(' ')
a.clear()
for i in range(0, n):
    a.append(int(b[i]))
ans = 0
for i in range(0, m):
    b = input().split(' ')
    c = []
    for j in range(0, 3):
        c.append(int(b[j]))
    ans = max(ans, (a[c[0] - 1] + a[c[1] - 1]) / c[2])
print(ans)
