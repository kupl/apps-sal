for _ in range(int(input())):
    (n, k) = map(int, input().split())
    if n % 2 == 0:
        print(n + n // 2 * k)
    elif n == 3:
        print(n + 3 * k)
    else:
        print(n + 3 * k + (n - 3) // 2 * k)
