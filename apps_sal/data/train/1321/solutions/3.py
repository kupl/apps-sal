for _ in range(int(input())):
    n = int(input())
    n = n - 1
    k = n * (n + 1) * (2 * n + 1)
    print(int(k / 6))
