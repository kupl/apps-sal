for _ in range(int(input())):
    a,b,c = map(int,input().split())
    p,q,r = map(int,input().split())
    if p < a or q < b or r < c:
        print(-1)
    else:
        print(p+q+r-(a+b+c))
