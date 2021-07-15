import sys
from bisect import bisect

n = int(input())
xxx = list(map(int, input().split()))
l = int(input())

reachable = [[bisect(xxx, x + l) - 1 for x in xxx]]
while reachable[-1][0] < n - 1:
    rp = reachable[-1]
    reachable.append(list(map(rp.__getitem__, rp)))

q = int(input())
buf = []
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    ans = 0
    for i in range(len(reachable) - 1, -1, -1):
        ria = reachable[i][a]
        if ria >= b:
            continue
        ans += 1 << i
        a = ria
    if a != b:
        ans += 1
    buf.append(ans)

print(('\n'.join(map(str, buf))))

