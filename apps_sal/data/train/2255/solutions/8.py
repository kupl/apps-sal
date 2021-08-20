from collections import Counter
n = int(input())
a = [*map(int, input().split())]
pre = [[0] * 2 ** 20, [1] + [0] * (2 ** 20 - 1)]
t = ans = 0
for i in range(n):
    t ^= a[i]
    ans += pre[i & 1][t]
    pre[i & 1][t] += 1
print(ans)
