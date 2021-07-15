# cook your dish here
t=int(input())
while t>0:
    t-=1 
    n=int(input())
    l=list(map(int,input().split()))
    a=min(l)
    h=n/a
    f=n//a
    if f==h:
        print(f)
    else:
        print(f+1)
