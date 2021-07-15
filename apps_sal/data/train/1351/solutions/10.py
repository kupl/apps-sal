# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l1=[0]*n
    for i in range(n):
        if(i in l):
            l1[i]=i
        else:
            l1[i]=0
    print(*l1)

