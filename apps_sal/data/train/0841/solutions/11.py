t = int(input())
for _ in range(t):
    s = input()
    if len(s) == 1:
        print(s)
    else:
        mod = 10 ** 9 + 7
        l = len(s)
        curr = 0
        for i in s:
            curr *= 10
            curr += int(i)
            curr %= mod
        ans = curr
        p1 = 1
        p2 = 1
        for i in range(l):
            p1 *= 10
            p1 %= mod
        for i in range(l - 1):
            p2 *= 10
            p2 %= mod
        for i in range(l - 1):
            curr -= p2 * int(s[i]) % mod
            curr *= 10
            curr += int(s[i])
            curr %= mod
            ans *= p1
            ans %= mod
            ans += curr
            ans %= mod
        print(ans)
