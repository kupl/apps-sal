for _ in range(int(input())):
    n, r, x, y = map(int, input().split())
    if x > 0:
        arr = set(list(map(int, input().split())))
    if y > 0:
        brr = set(list(map(int, input().split())))
    if x > 0 and y > 0:
        crr = list(arr.union(brr))
        t = n - len(crr)
        if t > r:
            print(r)
        else:
            print(t)
    elif x > 0 or y > 0:
        s = max(x, y)
        t = n - s
        if t > r:
            print(r)
        else:
            print(t)
    else:
        if n > r:
            print(r)
        else:
            print(n)
