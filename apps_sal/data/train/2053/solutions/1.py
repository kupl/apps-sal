import sys
import bisect
input = sys.stdin.readline

n,m=list(map(int,input().split()))
B=list(map(int,input().split()))
G=list(map(int,input().split()))

B.sort()
G.sort()

if max(B)>min(G):
    print(-1)
    return

ANS=sum(B)*m
MAX=B[-1]
first=m
for i in range(m):
    if G[i]>MAX:
        first=i
        break


if first==0:
    ANS+=sum(G[1:])-MAX*(m-1)
    ANS+=G[0]-B[-2]

    print(ANS)
    return

else:
    ANS+=sum(G[first:])-MAX*(m-first)

    print(ANS)


    
    

