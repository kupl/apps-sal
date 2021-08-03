try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        for x in range(1, n + 1):
            for y in range(0, n - x):
                print(' ', end='')
            if x % 2 == 0:
                for y in range(1, x + 1):
                    print(y, end='')
                print()
            else:
                for y in range(1, x + 1):
                    print(chr(64 + y), end='')
                print()
except:
    pass
