for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    d = []

    for i in range(n):
        if b[i] == 1:
            c.append(a[i])
        else:
            d.append(a[i])
    r = 100 - m
    if len(c) == 0 or len(d) == 0:
        print("no")
    elif min(c) + min(d) <= r:
        print("yes")
    else:
        print("no")
