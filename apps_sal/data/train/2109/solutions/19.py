q = int(input())
for i in range(q):
    a,b = list(map(int, input().split()))
    a,b = min(a,b), max(a,b)
    l,r = a-1,b+1
    while r-l != 1:
        t = (l+r) // 2
        if t*t < a*b:
            l = t
        else:
            r = t
    c = l
    l,r = a-1,b+1
    while r-l != 1:
        t = (l+r) // 2
        if t*(t+1) < a*b:
            l = t
        else:
            r = t
    d = l
    print((a-1 + max(d*2-a, c*2-1-a) + int(a==b)))

