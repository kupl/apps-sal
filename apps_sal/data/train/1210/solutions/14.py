for _ in range(int(input())):
    n, x = map(int, input().split())
    a, b = map(str, input().split())
    if (a == 'L' and b == 'H'):
        if (x % 2 == 0):
            print(x, 'E')
        else:
            print(x, 'H')
    elif (a == 'L' and b == 'E'):
        if (x % 2 == 0):
            print(x, 'H')
        else:
            print(x, 'E')
    elif (a == 'R' and b == 'H'):
        if ((n - x + 1) % 2 == 0):
            print((n - x) + 1, 'E')
        else:
            print((n - x) + 1, 'H')
    elif (a == 'R' and b == 'E'):
        if ((n - x + 1) % 2 == 0):
            print((n - x) + 1, 'H')
        else:
            print((n - x) + 1, 'E')
