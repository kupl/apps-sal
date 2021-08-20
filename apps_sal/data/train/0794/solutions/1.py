mod = pow(10, 9) + 7
for tt in range(int(input())):
    (n, m) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    d = [0 for i in range(n + 1)]
    for i in l:
        d[i] += 1
    ans = 1
    for i in range(2, n + 1):
        ans *= pow(d[i - 1], d[i])
        ans %= mod
    print(ans % mod)
