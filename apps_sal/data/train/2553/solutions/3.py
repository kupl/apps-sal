class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def fac(m):
            result = 1
            for i in range(1,m+1):
                result *= i
            return result
        def PrimeTell(m):
            if m == 1 or m == 4:
                return False
            if m == 2 or m == 3:
                return True
            for j in range(2, m//2):
                if m%j == 0:
                    return False
            return True
        Sum = 0
        for i in range(1,n+1):
            if PrimeTell(i):
                Sum += 1
        return fac(Sum)*fac(n-Sum)% (10**9 + 7)

