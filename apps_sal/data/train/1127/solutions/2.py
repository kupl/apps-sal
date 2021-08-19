for t in range(int(input())):
    a = input().split()
    if len(a) == 1:
        s = a[0].capitalize()
        print(s)
    else:
        for i in range(0, len(a) - 1):
            a[i] = a[i].capitalize()
            print(a[i][0], end='')
            print('.', end=' ')
        a[-1] = a[-1].capitalize()
        print(a[-1], end='')
        print('\r')
