try:
    for _ in range(int(input())):
        (r, co) = list(map(int, input().split()))
        (x, y) = list(map(int, input().split()))
        a = y
        b = x
        c = co - a - 1
        d = r - b - 1
        p = max(b, d)
        q = max(a, c)
        k = max(p, q)
        print(p + q)
except:
    pass
