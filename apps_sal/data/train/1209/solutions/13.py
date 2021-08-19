def test():
    (v1, t1, v2, t2, v3, t3) = list(map(int, input().split(' ')))
    req = v3 * t3
    if v1 + v2 < v3 or max(t1, t2) < t3:
        print('NO')
        return 0
    else:
        x = v3 * (t3 - t2) / (t1 - t2)
        y = v3 * (t3 - t1) / (t2 - t1)
        if x <= v1 and y <= v2 and (x >= 0) and (y >= 0):
            print('YES')
        else:
            print('NO')
    return 0


t = int(input())
for i in range(t):
    testy = test()
