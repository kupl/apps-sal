for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    f = 0
    t = 0
    p = 1
    for i in lst:
        if i == 5:
            f += 1
        elif i == 10:
            if f > 0:
                f -= 1
                t += 1
            else:
                p = 0
                break
        elif t > 0:
            t -= 1
        elif f > 1:
            f -= 2
        else:
            p = 0
            break
    if p == 1:
        print('YES')
    else:
        print('NO')
