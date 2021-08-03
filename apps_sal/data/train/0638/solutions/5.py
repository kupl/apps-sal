MOD = int(1e9 + 7)


def power(a, n):
    if(n == 0):
        return 1
    if(n == 1):
        return a
    x = power(a, n >> 1)
    x = (x * x)
    if(x >= MOD):
        x %= MOD
    if(n & 1):
        x = (x * a)
        if(x >= MOD):
            x %= MOD
    return x


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print("Case", _ + 1, end=":\n")
    for string in range(m):
        a = len(input())
        if(a > n):
            print(0)
            continue
        print(((n - a + 1) * power(26, n - a)) % MOD)
