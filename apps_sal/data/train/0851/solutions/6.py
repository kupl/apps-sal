for _ in range(int(input())):
    n, k = map(int, input().split())
    print(2 * (((k - 1) * (n - 1) + k) / k))

