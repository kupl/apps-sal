t = int(input())
for _ in range(t):
    (a, b, c, d) = map(int, input().split())
    dis = abs(a - b)
    sp = abs(c - d)
    if sp != 0:
        if dis % sp == 0:
            print('YES')
        else:
            print('NO')
    elif sp == 0 and a == b:
        print('YES')
    else:
        print('NO')
