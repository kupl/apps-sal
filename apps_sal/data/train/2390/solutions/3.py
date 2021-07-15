import sys
input = sys.stdin.readline
from collections import Counter

Q=int(input())
for testcase in range(Q):
    n=int(input())
    A=Counter((list(map(int,input().split()))))
    S=sorted(list(A.values()),reverse=True)

    #print(A)
    #print(S)
    NOW=10**10

    ANS=0
    for s in S:
        M=min(NOW,s)
        ANS+=M
        NOW=M-1

        if NOW==0:
            break

    print(ANS)
        

    

