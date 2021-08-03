N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MOD = 10**9 + 7


def gen_poly(a, b, c):
    poly = [0 for _ in range(c + 1)]
    for x in range(a, b + 1):
        xpow = 1
        for i in range(c + 1):
            poly[i] += xpow
            xpow = (xpow * x) % MOD
    for i in range(c + 1):
        poly[i] %= MOD
    return poly


def mult_polys(p1, p2, dmax):
    ans = [0 for _ in range(dmax + 1)]
    for i, c in enumerate(p1):
        for i2, c2 in enumerate(p2):
            if i + i2 <= dmax:
                ans[i + i2] += c * c2
            else:
                break
    ans = [x % MOD for x in ans]
    return ans


polys = [gen_poly(a, b, C) for a, b in zip(A, B)]
prodpoly = [1]
for poly in polys:
    prodpoly = mult_polys(prodpoly, poly, C)

print(prodpoly[C])
