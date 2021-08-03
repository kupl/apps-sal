n = int(input())
for i in range(n):
    t = int(input())
    m = list(map(int, input().split()))
    p, q = 0, 0
    if t == 1:
        if m[0] >= 0:
            print('YES')
        else:
            print('NO')
    else:
        for i in m:
            if i < 0:
                q += i
            else:
                p += i
        if p >= abs(q):
            print('YES')
        else:
            print('NO')
