import sys
import math
from collections import defaultdict
(n, m) = list(map(int, sys.stdin.readline().split()))
(up, down) = (1, n)
count = 0
while up <= down:
    (left, right) = (1, m)
    while left <= m and count < n * m:
        if count < n * m:
            sys.stdout.write(str(up) + ' ' + str(left) + '\n')
        count += 1
        left += 1
        if count < n * m:
            sys.stdout.write(str(down) + ' ' + str(right) + '\n')
        count += 1
        right -= 1
    up += 1
    down -= 1
"if n==1:\n    a=len(ans)\n    #print(a,'a')\n    for i in range(a//2):\n        print(ans[i][0],ans[i][1])\nelse:\n    a=len(ans)\n    for i in range(a//2):\n        print(ans[i][0],ans[i][1])\n    #print(ans)"
