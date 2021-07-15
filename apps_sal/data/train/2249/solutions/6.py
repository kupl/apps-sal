t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    if x==a:
        print(abs(y-b))
    elif y==b:
        print(abs(x-a))
    else:
        print(abs(x-a)+abs(y-b)+2)
