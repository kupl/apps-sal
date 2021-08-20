t = int(input())
for _ in range(t):
    k = int(input())
    for i in range(k):
        for j in range(int(k / 2) + 1):
            if i <= j:
                if i == j:
                    print('*', end='')
                elif i < j:
                    print(' ', end='')
            elif i + j == k - 1:
                print('*', end='')
            elif i > j:
                print(' ', end='')
        print()
