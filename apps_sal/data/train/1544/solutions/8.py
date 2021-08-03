t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i < (n - 1):
                if j == 0 or i == j:
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                print('*', end='')
        print()
