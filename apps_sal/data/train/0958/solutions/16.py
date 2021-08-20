try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 1
        while i <= n:
            j = i
            while j <= n - 1:
                print(' ', end='')
                j += 1
            print('*', end='')
            if i > 1 and i < n:
                for j in range((i - 1) * 2 - 1):
                    print(' ', end='')
                print('*', end='')
            if i == n:
                for j in range(2 * (i - 1)):
                    print('*', end='')
            print()
            i += 1
except EOFError:
    pass
