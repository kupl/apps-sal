mod = 1000000007
for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    x = k % mod * pow(k - 1, n - 1, mod)
    print(x % mod)
