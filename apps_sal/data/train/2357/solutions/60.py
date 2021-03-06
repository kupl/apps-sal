import itertools
(N, M, *A) = [int(_) for _ in open(0).read().split()]


class Factorial:

    def __init__(self, max_fact, mod):
        f = [1] * (max_fact + 1)
        for idx in range(2, max_fact + 1):
            f[idx] = f[idx - 1] * idx
            f[idx] %= mod
        if mod > max_fact:
            fi = [pow(f[-1], mod - 2, mod)]
            for idx in range(max_fact, 0, -1):
                fi += [fi[-1] * idx % mod]
            fi = fi[::-1]
        else:
            fi = [pow(n, mod - 2, mod) for n in f]
        self.mod = mod
        self.f = f
        self.fi = fi

    def factorial(self, n):
        return self.f[n]

    def factorial_inverse(self, n):
        return self.fi[n]

    def combination(self, n, r):
        f = self.f
        fi = self.fi
        mod = self.mod
        if n < r:
            return 0
        elif n < len(f):
            return f[n] * fi[r] * fi[n - r] % mod
        elif n < 2 * r:
            r = n - r
        if r < len(f):
            ret = fi[r]
            for _ in range(r):
                ret *= n
                ret %= mod
                n -= 1
            return ret
        else:
            1 / 0

    def permutation(self, n, r):
        f = self.f
        fi = self.fi
        mod = self.mod
        if n < len(f):
            return f[n] * fi[n - r] % mod
        elif r < len(f):
            ret = 1
            for _ in range(r):
                ret *= n
                ret %= mod
                n -= 1
            return ret
        else:
            1 / 0

    def homogeneous_product(self, n, r):
        f = self.f
        fi = self.fi
        return f[n + r - 1] * fi[r] * fi[n - 1] % self.mod


suma = sum(A)
max_fact = suma + N
mod = 10 ** 9 + 7
fact_instance = Factorial(max_fact, mod)
comb = fact_instance.combination
ans = comb(M + N, suma + N)
print(ans)
'\nans = 0\nfor bs in itertools.product(range(M + 1), repeat=N):\n    f = 0\n    if sum(bs) > M:\n        continue\n    ans += list(\n        itertools.accumulate([comb(b, a) for a, b in zip(A, bs)],\n                             func=lambda x, y: x * y % mod))[-1]\n    ans %= mod\nprint(ans)\n'
'\nans(N, M, sum(A))\n\nans(3, 1, 1) = C[4, 0]\nans(3, 2, 2) = C[5, 0]\nans(3, 3, 3) = C[6, 0]\n\nans(3, 4, 4) = C[7, 0]\n\nans(3, 6, 5) = C[9, 1]\nans(4, 6, 5) = C[10, 1]\n\nans(N, M, sum(A)) = C[N + M, M - sum(A)]\n'
