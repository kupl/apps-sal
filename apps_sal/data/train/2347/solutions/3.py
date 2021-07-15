import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n,k=list(map(int,input().split()))
    S=input().strip()

    A=[-1]*k

    for i in range(n):
        if S[i]=="0":
            if A[i%k]==1:
                print("NO")
                break
            else:
                A[i%k]=0

        if S[i]=="1":
            if A[i%k]==0:
                print("NO")
                break
            else:
                A[i%k]=1
    else:
        Z=0
        O=0
        for i in range(k):
            if A[i]==0:
                Z+=1
            if A[i]==1:
                O+=1
        if Z>k//2 or O>k//2:
            print("NO")
        else:
            print("YES")
            

