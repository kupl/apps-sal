for n in range(int(input())):
    v1, t1, v2, t2, v3, t3 = map(int, input().split())
    ok = 0
    if t1 <= t3 <= t2:
        x, y = t2 - t3, t3 - t1
        ok = x * v3 <= (x + y) * v1 and y * v3 <= (x + y) * v2
    print('YES' if ok else 'NO')
