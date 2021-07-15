class Solution:
    def get_ggT(self, a, b):
        while (a != b):
            a_ = a - b
            a = max(a_, b)
            b = min(a_, b)
            
        return a
        
        
        
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = set()
        
        
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                ggT = self.get_ggT(denominator, numerator)
                ret.add(str(numerator // ggT) + \"/\" + str(denominator // ggT))
                
        return ret
