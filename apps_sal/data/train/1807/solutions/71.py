from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        ans = []
        for i in range(1, n):
            if gcd(n, i) == 1:
                ans.append(f\"{i}/{n}\")
        ans += self.simplifiedFractions(n-1)
        return ans
