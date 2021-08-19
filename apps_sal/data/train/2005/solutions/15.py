import sys
import math
from collections import defaultdict, deque
import heapq
s = sys.stdin.readline()[:-1]
ans = 0
n = len(s)
mink = n
for i in range(n - 1, -1, -1):
    k = 1
    z = True
    while i + 2 * k < n and z:
        if s[i] == s[i + k] == s[i + 2 * k]:
            z = False
            continue
        k += 1
    if not z:
        mink = min(mink, i + 2 * k)
        # print(mink,'mink',i,'i')
    x = n - mink
    ans += x
    # ans+=(n-(i+2*k))+(i-1)
    # print(ans,'ans',i,'i')
print(ans)
