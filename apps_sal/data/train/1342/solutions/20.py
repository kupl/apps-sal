for i in range(int(input())):
    k = list(map(int, input().split()))
    n = k[0]
    x = k[1]
    l = list(map(int, input().split()))
    l.sort()
    i = 0
    v = 0
    c = 0
    t = 0
    for i in l:
        if x >= i:
            v = v + 1
            x = x * 2
        while x <= i:
            z = i - x
            c = c + 1
            x = x * 2
            if z * 2 <= i:
                i = z
                t = 1
            else:
                i = i
    print(c + v + t)
