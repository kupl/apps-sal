class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def Simplify(x, y):
            for i in range(x, 1, -1):
                if x % i == 0 and y % i == 0:
                    x //= i
                    y //= i 
            return x, y
        
        res = set()
        for i in range(2, n+1):
            for j in range(1, i):
                nom, denom = j, i
                print('before', nom, denom)
                nom, denom = Simplify(nom, denom) 
                print('after', nom, denom)
                res.add(str(nom)+\"/\"+str(denom))
        return res
    
    
                
[\"1/3\",\"2/4\",\"5/6\",\"5/8\"]

[\"1/3\",\"5/6\",\"5/8\"]
