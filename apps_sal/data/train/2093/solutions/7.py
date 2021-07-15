from sys import stdin
from collections import deque
from bisect import bisect_right  as br
n=int(stdin.readline().strip())
s=list(map(int,stdin.readline().strip().split()))
arr=deque([s[0]])
ans=deque([[s[0]]])
for i in range(1,n):
    x=br(arr,s[i])
    if x==0:
        arr.appendleft(s[i])
        ans.appendleft([s[i]])
    else:
        arr[x-1]=s[i]
        ans[x-1].append(s[i])
ans.reverse()
for i in ans:
    print(*i)
    

