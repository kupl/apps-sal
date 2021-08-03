class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = []
        decimals = set()
        
        for i in range(1, n + 1):
            for x in range (1, i + 1):
                if (x % i != 0 and x/i not in decimals):
                    decimals.add(x/i)
                    fractions.append(str(x) + \"/\" + str(i))
                    
        return fractions
    
            
