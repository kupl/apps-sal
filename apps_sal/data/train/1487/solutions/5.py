t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x = int(input())
    j = n - 1
    i = 0
    a = 0
    b = 0
    remain = 0
    while True:
        if i > j:
            break
        if i == j:
            if remain:
                a += 1
            elif b > a:
                b += 1
            else:
                a += 1
            break
        b += 1
        d = x * l[j] + remain
        while i < j:
            d -= l[i]
            if d == 0:
                remain = 0
                a += 1
                i += 1
                break
            if d < 0:
                remain = d + l[i]
                break
            a += 1
            i += 1
        j -= 1
    print(a, b)
