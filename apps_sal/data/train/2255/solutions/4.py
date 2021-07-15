n = int(input())
a = [int(x) for x in input().split()]
pred = [0]
for i in range(n):
    pred.append(a[i] ^ pred[-1])
d = {}
d1 = {}
a = pred[::2]
b = pred[1::2]
ans = 0
for i in a:
    d[i] = d.get(i, 0) + 1
for i in b:
    d1[i] = d1.get(i, 0) + 1
for i in d:
    ans += d[i] * (d[i] - 1) // 2
for i in d1:
    ans += d1[i] * (d1[i] - 1) // 2
print(ans)
