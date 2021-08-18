for i in range(int(input())):
    m, tc, th = [int(num) for num in input().split()]
    if th == tc:
        print('No')
    elif (th - tc) % 3 == 0 and ((th - tc) // 3) <= m:
        print('No')
    else:
        print('Yes')
