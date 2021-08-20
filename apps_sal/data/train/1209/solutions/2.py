for _ in range(int(input())):
    (v1, t1, v2, t2, v3, t3) = list(map(int, input().split()))
    if t3 >= min(t1, t2) and t3 <= max(t1, t2) and (v3 <= v1 + v2):
        p = t2 - t3
        q = t3 - t1
        if p * v3 <= (p + q) * v1 and q * v3 <= (p + q) * v2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
