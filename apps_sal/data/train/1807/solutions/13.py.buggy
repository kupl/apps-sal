class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            return y if x == 0 else gcd(y % x, x)
        
        return [\"%s/%s\" % (i, j) for j in range(2, n + 1) for i in range(1, j) if gcd(i, j) == 1]
