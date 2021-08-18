import sys
import math
from collections import defaultdict
n, m = list(map(int, sys.stdin.readline().split()))
up, down = 1, n
count = 0
while up <= down:
    left, right = 1, m
    while left <= m and count < n * m:
        if count < n * m:
            sys.stdout.write((str(up) + " " + str(left) + "\n"))
        count += 1
        left += 1
        if count < n * m:
            sys.stdout.write((str(down) + " " + str(right) + "\n"))
        count += 1
        right -= 1
    up += 1
    down -= 1
'''if n==1:
    a=len(ans)
    for i in range(a//2):
        print(ans[i][0],ans[i][1])
else:
    a=len(ans)
    for i in range(a//2):
        print(ans[i][0],ans[i][1])
