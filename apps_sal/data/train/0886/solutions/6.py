t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    p = -1
    q = -1
    for x in arr:
        x += x % 3
        if x < m:
            if p == -1 or x > p:
                p = x
        elif x > m:
            if q == -1 or x < q:
                q = x
    print(p, ' ', q)
    t -= 1
