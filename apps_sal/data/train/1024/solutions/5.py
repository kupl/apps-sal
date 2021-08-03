p, ip = 0, 0
for _ in range(int(input())):
    s, n, k, r = map(int, input().split())
    sm = 0
    while n != 0:
        sm += k
        k = r * k
        n -= 1
    if (s - sm) >= 0:
        print('POSSIBLE', s - sm)
        p += (s - sm)
    else:
        print('IMPOSSIBLE', abs(s - sm))
        ip += abs(s - sm)
if p >= ip:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
