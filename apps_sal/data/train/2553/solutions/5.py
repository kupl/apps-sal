class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                  61, 67, 71, 73, 79, 83, 89, 97]
        r = sum(1 for p in primes if p <= n)
        a = 10**9 + 7
        ans = 1
        for i in range(1, min(r, n - r) + 1):
            ans *= (i % a)**2
            ans %= a
        for i in range(min(r, n - r) + 1, max(r, n - r) + 1):
            ans *= i
            ans %= a
        return ans
