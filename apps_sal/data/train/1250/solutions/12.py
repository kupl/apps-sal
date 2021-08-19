t = int(input())
mod = 1000000007
while t:
    t -= 1
    n = int(input())
    ans = 2 * pow(3, n + 1, mod) % mod - pow(2, n + 2, mod) - (pow(3, n + 1, mod) - 1) * 500000004 % mod
    ans %= mod
    print(ans)
