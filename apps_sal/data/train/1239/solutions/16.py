T = int(input())

for t in range(T):
    N = int(input())

    for i in range(N, 0, -1):
        for j in range(i):
            print(' ', end='')
        for j in range(N, i - 1, -1):
            print(j, end='')
        print()
    for i in range(N + 1):
        for j in range(i):
            print(' ', end='')
        for j in range(N, i - 1, -1):
            print(j, end='')
        print()
