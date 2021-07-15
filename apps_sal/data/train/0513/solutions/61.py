from collections import deque
import bisect

N=int(input())
A=list(map(int,input().split()))
ans=[0]*N
Edge=[[] for _ in range(N)]
loute=[str(0)]*N
for i in range(N-1):
    u,v=map(int,input().split())
    Edge[u-1].append(v-1)
    Edge[v-1].append(u-1)
  
tmp=deque(str(0))
CHN=deque()
LIS=[10**18]*N
label=[False]*N
while tmp:
    T0=int(tmp[-1])
    if label[T0]:
        tmp.pop()
        pos,Val=CHN.pop()
        LIS[pos]=Val
        continue

    pos=bisect.bisect_left(LIS,A[T0])
    CHN.append((pos,LIS[pos]))
    LIS[pos]=A[T0]
    ans[T0]=bisect.bisect_left(LIS,10**18)

    if Edge[T0]:
        for i in Edge[T0]:
            if label[i]==False:
                tmp.append(i)
        label[T0]=True
    else:
        label[T0]=True
    
for i in range(N):
    print(ans[i])
