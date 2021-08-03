t = int(input())
for _ in range(t):
    k = int(input())
    for i in range(k):
        for j in range(2 * k - 1):
            if i < k - 1:

                if i + j < k - 1:
                    print(' ', end='')
                elif i + j == k - 1:
                    print('*', end='')
                elif i + j > k - 1 and i + j < k - 1 + (2 * i):
                    print(' ', end='')
                elif i + j == k - 1 + (2 * i):
                    print('*', end='')
            else:
                print('*', end='')
        print()
