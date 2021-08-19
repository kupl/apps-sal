for _ in range(int(input())):
    n = int(input())
    x = 0
    for _ in range(1, n + 1):
        if _ <= (n + 1) // 2:
            print(' ' * x, end='')
            print('*')
            x += 1
        else:
            if _ == (n + 1) // 2 + 1:
                x = x - 2
            print(' ' * x, end='')
            print('*')
            x -= 1
