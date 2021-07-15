ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
from collections import Counter as C
n = ii()
a = li()
oe = [C(), C()]
oe[1][0] = 1
x = 0
ans = 0
for i in range(n):
    x ^= a[i]
    ans += oe[i % 2][x]
    oe[i % 2][x] += 1
print(ans)
