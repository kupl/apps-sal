# 3:22
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        
        def simplified(i, n):
            for j in range(2, i + 1):
                if i % j == 0 and n % j == 0:
                    return False
            return True
        
        at_n = []
        for i in range(1, n):
            if simplified(i, n):
                at_n.append(f\"{i}/{n}\")
        
        return at_n + self.simplifiedFractions(n - 1)
