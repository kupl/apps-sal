class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            if b == 0:
                return a
            else:
                return gcd(b, a - b)
            
        output = []
        for den in range(1, n + 1):
            for num in range(1, den):
                if gcd(den, num) == 1:
                    output.append(\"%d/%d\" % (num, den))
        return output
