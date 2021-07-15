import sys
input = sys.stdin.readline

mod=998244353

t=int(input())
for tests in range(t):
    n,k=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    X=[-1]*(n+1)
    for i in range(n):
        X[A[i]]=i

    for i in range(k):
        B[i]=X[B[i]]

    Y=[0]*n
    for b in B:
        Y[b]=1
        
    Y.append(1)

    #print(Y)
    #print(B)

    ANS=0
    for b in B:
        #print(b,Y)
        if Y[b-1]==1 and Y[b+1]==1:
            print(0)
            break

        elif Y[b-1]==0 and Y[b+1]==0:
            ANS+=1

        Y[b]=0

    else:
        print(pow(2,ANS,mod))

    

