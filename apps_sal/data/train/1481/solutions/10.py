for _ in range(int(input())):
    s = input()
    l = len(s)
    if l % 2 == 1:
        print(-1)
    else:
        c1 = s.count('1')
        c0 = l - c1
        if c0 == 0 or c1 == 0:
            print(-1)
        elif c1 == c0:
            print(0)
        else:
            print(abs(c1 - c0) // 2)
