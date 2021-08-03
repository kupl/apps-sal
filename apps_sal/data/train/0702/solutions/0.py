for i in range(int(input())):
    m, tc, th = map(int, input().split())
    x = (th - tc)
    if x % 3 != 0:
        print("Yes")
    else:
        if (x // 3) <= m:
            print("No")
        else:
            print("Yes")
