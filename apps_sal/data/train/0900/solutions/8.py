def power(val, p, mod):
    ans = 1
    while p:
        if p & 1:
            ans = ans * val % mod
        val = val * val % mod
        p >>= 1
    return ans


t = int(input())
for i in range(t):
    k = int(input())
    print(10 * power(2, k - 1, 1000000007) % 1000000007)
