t=int(input())
while t!=0:
    a,b=map(int,input().split())
    print(max(a,b),a+b)
    t-=1
