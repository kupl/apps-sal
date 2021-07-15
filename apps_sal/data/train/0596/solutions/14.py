# cook your dish here
t=int(input())
M=1000000007
for z in range(t):
    N,K=list(map(int,input().split()))
    if N==0:
        K=K-1
        t=(K*(K+1))%M
        print(t)
        continue
    if K%2==0:
        s=N+K//2-1
        t=((s*(s+1))%M+N)%M
    else:
        s=N+K//2
        t=((s*(s+1))%M-N)%M
    print(t)
