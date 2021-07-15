import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

LIST=[]
for i in range(n):
    if A[i]==1:
        LIST.append(i)


k=len(LIST)

import math

FLIST=[k]

for j in range(2,2+int(math.sqrt(k))):
    if k%j==0:
        FLIST.append(j)
        if k//j>1:
            FLIST.append(k//j)

ANS=0
if FLIST==[1]:
    print(-1)

else:
    A=1<<35
    for f in FLIST:
        ANS=0

        if f==2:
            for i in range(len(LIST)):
                if i%2==1:
                    ANS+=LIST[i]-LIST[i-1]

            A=min(A,ANS)

        elif f%2==1:
            for i in range(len(LIST)):
                ANS+=abs(LIST[i]-LIST[i//f*f+f//2])

            A=min(A,ANS)

    print(A)
    

