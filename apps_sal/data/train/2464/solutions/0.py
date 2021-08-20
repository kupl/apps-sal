class Solution:

    def countPrimes(self, x):
        x = max(0, x - 1)
        if type(x) is not int:
            x = int(x)
        if x < 6:
            return [0, 0, 1, 2, 2, 3][x]

        def Phi(m, b):
            if not b:
                return m
            if not m:
                return 0
            if m >= 800:
                return Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
            t = b * 800 + m
            if not Phi_memo[t]:
                Phi_memo[t] = Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
            return Phi_memo[t]
        root2 = int(x ** (1.0 / 2))
        root3 = int(x ** (1.0 / 3))
        top = x // root3 + 1
        sieve = [0, 0] + [1] * (top - 2)
        pi = [0, 0]
        primes = []
        t = 0
        for i in range(2, top):
            if sieve[i] == 1:
                t += 1
                primes.append(i)
                sieve[i::i] = [0] * len(sieve[i::i])
            pi.append(t)
        (a, b) = (pi[root3 + 1], pi[root2 + 1])
        Phi_memo = [0] * ((a + 1) * 800)
        return Phi(x, a) + a - 1 - sum((pi[x // p] - pi[p] + 1 for p in primes[a:b]))
