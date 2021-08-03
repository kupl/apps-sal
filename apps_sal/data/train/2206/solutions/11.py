from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
ans = [0 for _ in range(n + 1)]
ans[0] = 1
ans[-1] = 1
sample = [0 for _ in range(n)]
last = n - 1
q = list(map(int, input().split()))
for i in range(n - 1):
    x = q[i]
    sample[x - 1] = 1
    if x - 1 == last:
        while sample[x - 1] != 0:
            x -= 1
        last = x - 1
    target = n - i - 2
    #print(last, target)
    ans[i + 1] = last - target + 1
print(*ans)
