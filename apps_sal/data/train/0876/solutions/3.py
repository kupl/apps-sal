# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    p=list(map(int,input().split()))
    pmax=max(p)
    pmin=min(p)
    if (pmax-pmin)<x:
        print("YES")
    else:
        print("NO")

