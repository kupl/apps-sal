n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = 10**9+7

s = sum(A)
ans = 1

def comb(n, r, mod):
    c = 1
    for i in range(r):
        c *= n-i
        c %= mod

    d = 1
    for i in range(1, r+1):
        d *= i
        d %= mod

    return (c * pow(d, mod-2, mod)) % mod


print((comb(m+n, s+n, mod)))


