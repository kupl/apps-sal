t=int(input())
for i in range(t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    if max(a)-min(a)<x:
        print("YES")
    else:
        print("NO")

