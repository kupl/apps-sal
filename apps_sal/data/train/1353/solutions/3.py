def time(x1, y1, x2, y2):
    if x1 == x2:
        return y2 - y1
    return y2 - y1 + 1


ans = ['no', 'yes']
for _ in range(int(input())):
    t, fx, fy, sx, sy, f = 0, 1, 1, 2, 1, 1
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        if f:
            if a[1] == a[3] and a[2] == a[4]:
                f = 0
                continue
            if fy > a[2] or sy > a[4]:
                f = 0
                continue
            t1 = time(fx, fy, a[1], a[2])
            t2 = time(sx, sy, a[3], a[4])
            _t = a[0] - t
            if t1 > _t or t2 > _t:
                f = 0
        t, fx, fy, sx, sy = a
    print(ans[f])
