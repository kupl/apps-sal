class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        res = []
        for i in range(1, n):
            for j in range (i + 1, n + 1):
                g = gcd(i, j)
                a, b = i // g, j // g
                s = str(a) + \"/\" + str(b)
                
                if s not in res:
                    res.append(s)
        return res
