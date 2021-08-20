T = int(input())
while T > 0:
    T -= 1
    (A, B, C, D) = map(int, input().split())
    res1 = max(C, D)
    res2 = min(C, D)
    val1 = B - A
    val2 = res2 - res1
    val1 = abs(val1)
    val2 = abs(val2)
    if val2 != 0:
        if val1 % val2 == 0:
            print('YES')
        else:
            print('NO')
    elif val1 == 0 and val2 == 0:
        print('YES')
    else:
        print('NO')
