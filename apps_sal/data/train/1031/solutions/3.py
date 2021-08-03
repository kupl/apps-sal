t = int(input())
for i in range(t):
    h, s = list(map(int, input().split()))
    d = ((h**4) - (16 * s * s))
    if d < 0:
        print("-1")
    else:
        d = d**0.5
        r1 = ((h**2) + d) / 2
        r2 = ((h**2) - d) / 2
        if r1 < 0 or r2 < 0:
            print("-1")
        else:
            arr = []
            r1 = r1**0.5
            r2 = r2**0.5
            arr.append(r1)
            arr.append(r2)
            arr.append(h)
            arr.sort()
            print('%.6f' % arr[0], '%.6f' % arr[1], '%.6f' % arr[2])
