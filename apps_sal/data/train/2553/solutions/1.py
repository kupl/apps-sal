class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # there are 25 primes from 1 to 100

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        for i in range(len(primes)):
            if primes[i] > n:
                break
        count = i
        print(count)
        return math.factorial(count) % (10**9 + 7) * math.factorial(n - count) % (10**9 + 7)
