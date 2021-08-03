from itertools import accumulate
import sys
input = sys.stdin.readline
s = input()[:-1]
t = input()[:-1]
d = {"A": 1, "B": 2}
ds = [0] + list(accumulate([d[x] for x in s]))
dt = [0] + list(accumulate([d[x] for x in t]))
ans = []
append = ans.append
for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if (ds[b] - ds[a - 1]) % 3 == (dt[d] - dt[c - 1]) % 3:
        append("YES")
    else:
        append("NO")
print(("\n".join(ans)))
