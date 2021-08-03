class Factorials:
    def __init__(self, n=10**6, mod=10**9 + 7):
        self.mod = mod

        # self.fac[i] ≡ i! (factorial:階乗)
        self.fac = [1] * (n + 1)
        for i in range(2, n + 1):
            self.fac[i] = self.fac[i - 1] * i % mod

        """
        # self.rec[i] ≡ 1 / i! (reciprocal:逆数)
        self.rec = [1] * (n+1)
        self.rec[n] = pow(self.fac[n], mod-2, mod)
        for i in range(n-1, 1, -1):
            self.rec[i] = self.rec[i+1] * (i+1) % mod

    # self.comb(n, r) ≡ nCr
    def comb(self, n, r):
        return self.fac[n] * self.rec[r] * self.rec[n-r] % self.mod
    
    # self.perm(n, r) ≡ nPr
    def perm(self, n, r):
        return self.fac[n] * self.rec[n-r] % self.mod

    # self.inv(n) ≡ 1 / n ≡ pow(n, mod-2, mod)
    def inv(self, n):
        return self.fac[n-1] * self.rec[n] % self.mod
    """


mod = 10**9 + 7


def fact(n, r):
    res = 1
    for i in range(r):
        res *= n - i
        res %= mod
    return res


n, m = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)
if m < sum_a:
    print(0)
    return

fct = Factorials(sum_a + n)

print(fact(n + m, sum_a + n) * pow(fct.fac[sum_a + n], mod - 2, mod) % mod)
