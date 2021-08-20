def cmb(x, y):
    if x < y:
        return 0
    bunsi = 1
    bunbo = 1
    for i in range(1, y + 1):
        bunsi = bunsi * (x + 1 - i) % mod
        bunbo = bunbo * i % mod
    res = bunsi * pow(bunbo, mod - 2, mod) % mod
    return res


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
s = sum(a)
ans = cmb(m + n, s + n)
print(ans)
