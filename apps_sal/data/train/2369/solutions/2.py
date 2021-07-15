import sys
input = sys.stdin.readline
import heapq
from collections import Counter

Q=int(input())
for testcase in range(Q):
    n=int(input())
    C=[list(map(int,input().split())) for i in range(n)]

    D=[[0,0] for i in range(n+1)]

    for x,y in C:
        D[x][0]+=1
        if y==1:
            D[x][1]+=1

    W=[]
    for i in range(n+1):
        if D[i][0]!=0:
            W.append((D[i][0],D[i][1]))

    W.sort(reverse=True)
    W.append((0,0))
    #print(W)

    C2=Counter([c[0] for c in C])
    S=sorted(list(C2.values()),reverse=True)

    NOW=10**10

    ANS=[]
    for s in S:
        M=min(NOW,s)
        ANS.append(M)
        NOW=M-1

        if NOW==0:
            break

    #print(ANS,sum(ANS))

    H=[]
    i=0
    ANS1=0
    for ans in ANS:
        while W[i][0]>=ans:
            heapq.heappush(H,-W[i][1])
            i+=1

        x=min(ans,-heapq.heappop(H))
        ANS1+=x
    print(sum(ANS),ANS1)
            
            

        

    

