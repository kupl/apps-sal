t = int(input())
for i in range(t):
    l = input()
    if len(l) % 2 == 1:
        print(-1)
    else:
        z = l.count("1")
        s = len(l)
        if s == z or z == 0:
            print(-1)
        else:
            print(abs(s - 2 * z) // 2)
