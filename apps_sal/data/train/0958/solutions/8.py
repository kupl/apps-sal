def printPattern(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(' ', end='')
        if i == 1 or i == n:
            for j in range(1, i * 2):
                print('*', end='')
        else:
            for j in range(1, i * 2):
                if j == 1 or j == i * 2 - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()


t = int(input())
for _ in range(t):
    printPattern(int(input()))
