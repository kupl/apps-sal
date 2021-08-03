for _ in range(int(input())):
    n, k = map(int, input().split())
    print((2 * (n * k - n + 1)) / k)
