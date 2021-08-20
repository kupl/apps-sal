for _ in range(int(input())):
    (n, l, r) = map(int, input().split())
    print(n - l + pow(2, l) - 1, pow(2, r) - 1 + (n - r) * pow(2, r - 1))
