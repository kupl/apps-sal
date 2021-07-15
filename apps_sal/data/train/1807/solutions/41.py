class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        output = []
        for n in range(2,n+1):
            for m in range(1,n):
                if math.gcd(n,m) == 1:
                    output.append(str(m) + '/' + str(n))
                    
        return output
