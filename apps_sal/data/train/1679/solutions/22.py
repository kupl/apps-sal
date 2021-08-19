for _ in range(int(input())):
    (n, k, x) = map(int, input().split())
    for i in range(n):
        if (i + 1) % k == 0 and i != n - 1:
            print(x, end=' ')
        elif i == n - 1:
            print(x if n % k == 0 else 0)
        else:
            print(0, end=' ')
