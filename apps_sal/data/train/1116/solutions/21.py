from collections import defaultdict
n = int(input())
li = list(int(i) for i in input().split())

pre = defaultdict(int)
ans, cur = 0, 0
for i in range(n):
    cur += li[i]
    if cur == 0:
        ans += 1
    if cur in pre:
        ans += pre[cur]
    pre[cur] += 1
print(ans)
