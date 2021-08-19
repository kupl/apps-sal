(n, p, k) = map(int, input().split())
d = {}
ans = 0
b = list(map(int, input().split()))
for i in range(n):
    a = b[i]
    val = (a ** 4 - k * a) % p
    if d.get(val) == None:
        d[val] = 1
    else:
        ans += d[val]
        d[val] += 1
print(ans)
