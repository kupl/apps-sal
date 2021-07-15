n=int(input())
for i in range(n):
    g1,g2=map(int,input().split())
    s=0
    if g1<g2:
        s=g2
    else:
        s=g1
    print(s,g1+g2)
