t=int(input())
while(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    if(max(a)==max(b)):
        print("NO")
    else:
        print("YES")
    t-=1
