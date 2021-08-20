for t in range(int(input())):
    (n, k) = map(int, input().split())
    a = k - 1
    b = k * 2
    c = k + n - 1
    d = b - c - 1
    print(a + d * (d + 1) // 2 % 1000000007)
