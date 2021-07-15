# cook your dish here
for i in range(int(input())):
    N,K=map(int,input().split())
    lst=list(map(int,input().split()))
    p=max(lst)+K
    q=min(lst)-K
    print(abs(p-q))
