t = int(input())
while t:
    n = int(input())
    for i in range(1, n + 1):
        if i == n:
            print('*' * (2 * i - 1), end='')
            print()
            continue
        if i == 1:
            print(' ' * (n - 1), end='')
            print('*', end='')
            print()
            continue
        for j in range(n - i):
            print(' ', end='')
        print('*' + ' ' * (2 * i - 3) + '*', end='')
        print()
    t -= 1
