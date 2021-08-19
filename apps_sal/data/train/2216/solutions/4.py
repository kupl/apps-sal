import sys
import math
s = input()
k = [[0, 0, 0]]
v = [0] * 3
for i in range(len(s)):
    v[ord(s[i]) - ord('x')] += 1
    k.append(list(v))
m = int(input())
for i in range(m):
    (l, r) = [int(x) for x in sys.stdin.readline().split()]
    vmin = min([k[r][0] - k[l - 1][0], k[r][1] - k[l - 1][1], k[r][2] - k[l - 1][2]])
    vmax = max([k[r][0] - k[l - 1][0], k[r][1] - k[l - 1][1], k[r][2] - k[l - 1][2]])
    if r - l + 1 <= 2 or vmax - vmin < 2:
        print('YES')
    else:
        print('NO')
