t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1):
        print(l[i],end="")
    print(l[n-1])
