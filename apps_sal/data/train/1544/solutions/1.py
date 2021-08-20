def solve():
    n = int(input())
    i = 0
    while i < n - 1:
        if i == 0:
            print('*', end='')
        else:
            print('*', end='')
            for k in range(i - 1):
                print(' ', end='')
            print('*', end='')
        print()
        i += 1
    for i in range(n):
        print('*', end='')
    print()


t = int(input())
i = 0
while i < t:
    solve()
    i += 1
