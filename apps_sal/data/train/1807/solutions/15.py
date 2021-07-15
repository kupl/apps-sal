class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = []
        
        def gcd(numerator, denominator):
            if numerator == 0:
                return denominator
            return gcd(denominator % numerator, numerator)
            
            
            
            
        for numerator in range(1, n + 1):
            for denominator in range(numerator + 1, n + 1):
                if numerator != denominator:
                    if gcd(numerator, denominator) == 1:
                        ret.append(str(numerator) + '/' + str(denominator))
        return ret
