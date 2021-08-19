MOD = 10 ** 9 + 7
for lo in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if n == 0:
        print(k * (k - 1) % MOD)
        continue
    c = k // 2
    x = 1
    if k % 2 == 0:
        x = 0
    y = c + x + n
    if x == 0:
        ans = y * (y - 1) + n
    else:
        ans = y * (y - 1) - n
    print(ans % MOD)
