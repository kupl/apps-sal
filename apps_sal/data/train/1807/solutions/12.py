class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        ret = []
        
        for i in range(2, n + 1):
            if i in primes:
                ret += [\"%d/%d\" % (j, i) for j in range(1, i)]
            else:
                tmpPrimes = []
                for p in primes:
                    if p * 2 > i:
                        break
                    if i % p == 0:
                        tmpPrimes.append(p)
                tmp = set(range(1, i))
                for p in tmpPrimes:
                    for j in range(p, i, p):
                        tmp.discard(j)
                ret += [\"%d/%d\" % (j, i) for j in tmp]
        return ret
