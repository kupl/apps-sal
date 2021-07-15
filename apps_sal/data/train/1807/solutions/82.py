from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = []
        for numerator in range(1, n + 1):
            for denominator in range(numerator + 1, n + 1):
                if numerator != denominator:
                    if gcd(numerator, denominator) == 1:
                        ret.append(str(numerator) + '/' + str(denominator))
        return ret
