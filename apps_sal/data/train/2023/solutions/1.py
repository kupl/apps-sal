import math
n = int(input())
m = math.ceil(math.sqrt(n))
ans = []
for k in range(m):
    s = min((k + 1) * m, n)
    t = k * m
    ans.extend(list(range(s, t, -1)))
print(*ans)
