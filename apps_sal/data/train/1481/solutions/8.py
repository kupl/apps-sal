for _ in range(int(input())):
    s = str(input())
    if len(s) & 1 == 1:
        print(-1)
    else:
        z = 0
        o = 0
        for i in range(len(s)):
            if s[i] == '0':
                z += 1
            else:
                o += 1
        if z == o:
            print(0)
        elif (z or o) != len(s):
            print(int(abs(z - o) / 2))
        else:
            print(-1)
