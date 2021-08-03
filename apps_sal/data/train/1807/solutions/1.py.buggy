class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        if n == 1:
            return []
        k = 0
        ret = []
        for i in range(2, n + 1):
            if i in primes:
                ret += [\"%d/%d\" % (j, i) for j in range(1, i)]
            else:
                dPrimes = []
                for p in primes:
                    if p * 2 > i:
                        break
                    if i % p == 0:
                        dPrimes.append(p)
                tmp = set(range(1, i))
                for p in dPrimes:
                    for j in range(p, i, p):
                        tmp.discard(j)
                ret += [\"%d/%d\" % (j, i) for j in tmp]
        return ret
