def go():
    n,x = list(map(int,input().split()))
    a = set(map(int,input().split()))
    ma = max(a)
    cand = ((x+ma-1)//ma)
    if cand==1 and x not in a:
        cand =2
    print (cand)

t = int(input())

for _ in range(t):
    go()


