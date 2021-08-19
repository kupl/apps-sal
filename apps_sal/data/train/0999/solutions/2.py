for _ in range(int(input())):
    n = int(input())
    k = n
    m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while k > 0:
        if (n - k + 1) % 2 == 0:
            print(' ' * (k - 1), end='')
            print(*list(range(1, n - k + 2)), sep='')
        else:
            print(' ' * (k - 1), end='')
            print(m[:n - k + 1])
        k = k - 1
