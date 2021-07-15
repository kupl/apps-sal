import sys
input = sys.stdin.readline
import bisect

t=int(input())
for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    compression_dict={a: ind for ind, a in enumerate(sorted(set(A)))}
    A=[compression_dict[a] for a in A]

    Q=[0]*n
     
    for i in range(n):
        Q[A[i]]=i
     
    count=1
    Ans=0
    #print(A,Q)
    for i in range(1,n):
        if Q[i]>Q[i-1]:
            count+=1
        else:
            Ans=max(count,Ans)
            count=1

    Ans=max(count,Ans)
     
    print(n-Ans)

    

