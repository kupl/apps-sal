for _ in range(int(input())):
    (n, k) = map(int, input().split(' '))
    print(2 + (n - 1) * (2 * (k - 1) / k))
