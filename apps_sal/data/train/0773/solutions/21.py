t = int(input())
while t:
    n = int(input())
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            print(i, i - 1, end=' ')
    else:
        for i in range(2, n - 2, +2):
            print(i, i - 1, end=' ')
        print(n - 1, n, n - 2, end=' ')
    print()
    t = t - 1
