M = int(1e9 + 7)
def I(): return list(map(int, input().split()))


n = I()[0]
d, e = {}, {}
for i in range(-500000, 500001):
    d[i], e[i] = 0, 0
for i in range(n):
    a, b = I()
    d[a] += 1
    e[b] += 1

ans, cnt = 0, 0

for i in range(-500000, 500001):
    if(d[i]):
        cnt += d[i]
    ans += cnt
    if(ans >= M):
        ans -= M
    if(ans < 0):
        ans += M
    if(e[i]):
        cnt -= e[i]
print(ans)
