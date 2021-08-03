t = int(input())
while t > 0:

    m, tc, th = map(int, input().split())

    if (th - tc) % 3 == 0:
        if (th - tc) // 3 <= m:
            print('No')
        else:
            print('Yes')
    else:
        print('Yes')

    t -= 1
