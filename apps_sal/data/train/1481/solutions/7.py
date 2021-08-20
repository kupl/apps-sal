for t in range(int(input())):
    s = input()
    z = s.count('0')
    o = s.count('1')
    if len(s) % 2 == 0:
        if z == 0 or o == 0:
            print(-1)
        else:
            print(len(s) // 2 - min(o, z))
    else:
        print(-1)
