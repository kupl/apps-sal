for testcase in range(int(input())):
    a, b, c, d = list(map(int, input().split()))

    val = abs(c - d)

    if a != b and c == d:
        print('NO')
    elif val == 0:
        print('YES')
    else:
        if abs(a - b) % val == 0:
            print('YES')
        else:
            print('NO')

