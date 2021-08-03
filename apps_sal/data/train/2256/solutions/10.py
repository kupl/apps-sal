import sys
import math
from collections import defaultdict
n, m = list(map(int, sys.stdin.readline().split()))
# cur=[1,1]
#ans=[-1 for _ in range(2*n*m)]
up, down = 1, n
count = 0
while up <= down:
    left, right = 1, m
    # ans.append(cur)
    while left <= m and count < n * m:
        # ans.append([up,left])
        # ans[count]=[up,left]
        if count < n * m:
            sys.stdout.write((str(up) + " " + str(left) + "\n"))
        count += 1
        left += 1
        # ans[count]=[down,right]
        if count < n * m:
            sys.stdout.write((str(down) + " " + str(right) + "\n"))
        count += 1
        # ans.append([down,right])
        right -= 1
    up += 1
    down -= 1
'''if n==1:
    a=len(ans)
    #print(a,'a')
    for i in range(a//2):
        print(ans[i][0],ans[i][1])
else:
    a=len(ans)
    for i in range(a//2):
        print(ans[i][0],ans[i][1])
    #print(ans)'''
