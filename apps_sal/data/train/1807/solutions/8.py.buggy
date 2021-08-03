class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for j in range(2,n+1):
            for i in range(1,j):
                if math.gcd(i,j) == 1:
                    res.append(str(i)+\"/\"+str(j))
        return res
