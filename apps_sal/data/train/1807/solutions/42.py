class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a: int, b: int) -> int:
            if a < b:
                a, b = b, a
            if b == 0:
                return a
            return gcd(b, a % b)
        
        out = []
        for denom in range(2, n + 1):
            for num in range(1, denom):
                if gcd(denom, num) == 1:
                    out.append(str(num) + '/' + str(denom))
        return out
