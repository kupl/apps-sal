for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i - 1, end=' ')
            else:
                print(i + 1, end=' ')
    else:
        for j in range(1, n - 1):
            if j % 2 == 0:
                print(j - 1, end=' ')
            else:
                print(j + 1, end=' ')
        print(n, end=' ')
        print(n - 2, end=' ')
    print()
