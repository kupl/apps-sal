for i in range(int(input())):
    nx = input().split()
    n = int(nx[0])
    x = int(nx[1])
    lrhe = input().split()
    lr = lrhe[0]
    he = lrhe[1]
    if lr == 'L':
        print(x, end=' ')
        if x % 2 != 0:
            print(he)
        elif he == 'H':
            print('E')
        else:
            print('H')
    if lr == 'R':
        print(n - x + 1, end=' ')
        if n % 2 == 0:
            if x % 2 == 0:
                print(he)
            elif he == 'H':
                print('E')
            else:
                print('H')
        elif x % 2 == 0:
            if he == 'H':
                print('E')
            else:
                print('H')
        else:
            print(he)
