for _ in range(int(input())):
    abc = sorted([int(x) for x in input().split()])
    if 0 in abc:
        print('NO')
    elif abc[-1] * abc[-1] == abc[0] * abc[0] + abc[1] * abc[1]:
        print('YES')
    else:
        print('NO')
