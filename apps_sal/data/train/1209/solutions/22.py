for _ in range(int(input())):
    v1, t1, v2, t2, v3, t3 = list(map(int, input().split()))
    if v1 + v2 < v3 or t3 > max(t1, t2) or t3 < min(t1, t2):
        print('NO')
    else:
        num = (t3 - t1)
        den = (t2 - t3)
        if v2 * (t2 - t1) >= v3 * (t3 - t1) and v1 * (t2 - t1) >= v3 * (t2 - t3):
            print('YES')
        else:
            print('NO')
