class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
               
        return [f\"{j}/{d}\" for d in range(2, n+1) for j in range(1, d) if gcd(max(d,j), min(d,j)) == 1]
                    

