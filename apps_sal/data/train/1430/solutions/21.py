for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    if n % 2 == 0:
        print(k * (n // 2) + n)

    if n % 2 == 1:
        print(k * (n // 2) + 2 * k + n)
