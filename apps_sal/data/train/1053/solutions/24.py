t=int(input())
while(t):
    n=int(input())
    a=[]
    p=0
    a=list(map(int,input().split()))
    for i in range(0,n):
        if(a[i]==0):
           p=p+1
    print(p)
    t=t-1

