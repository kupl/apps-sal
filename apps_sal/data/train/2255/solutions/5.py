n = int(input())
a = list(map(int, input().split()))
prev = [0]
for i in range(n):
    prev.append(a[i] ^ prev[-1])
var = {}
var1 = {}
a = prev[::2]
b = prev[1::2]
ans = 0
for c in a:
    var[c] = var.get(c, 0) + 1
for x in b:
    var1[x] = var1.get(x, 0) + 1
for c in var:
    ans += var[c] * (var[c] - 1) // 2
for c in var1:
    ans += var1[c] * (var1[c] - 1) // 2
print(ans)
