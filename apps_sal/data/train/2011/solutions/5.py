import sys
import math
n = int(input())
ans = []
for i in range(min(n, 100)):
    p = n - i
    s = p
    while p > 0:
        s += p % 10
        p = p // 10
    if s == n:
        ans.append(n - i)
print(len(ans))
ans.sort()
for x in ans:
    print(x)
