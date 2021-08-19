def pal(s):
    f = 0
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            f = 1
            break
    if f == 0:
        return 1
    else:
        return 0


for _ in range(int(input())):
    s = input()
    a = pal(s)
    if a == 1:
        print('YES')
    else:
        f = 0
        for i in range(len(s) - 1):
            s2 = s[0:i] + s[i + 1:len(s)]
            a = pal(s2)
            if a == 1:
                f = 1
                break
        if f == 0:
            print('NO')
        else:
            print('YES')
