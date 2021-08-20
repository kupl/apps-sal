try:
    T = int(input())
    while T != 0:
        l = list(map(int, input().split()))
        m = l[0]
        tc = l[1]
        th = l[2]
        flag = False
        if (th - tc) % 3 != 0:
            print('Yes')
        elif (th - tc) // 3 <= m:
            print('No')
        else:
            print('Yes')
        T -= 1
except:
    pass
