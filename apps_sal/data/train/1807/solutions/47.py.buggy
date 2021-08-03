class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for num in range(2, n+1):
            for i in range(1, num):
                if i == 1 or self.valid(i, num):
                    res.append(\"{}/{}\".format(i, num))
        return res
    
    def valid(self, a, b):
        if b % a == 0:
            return False
        for x in range(2, a):
            if a % x == 0 and b % x == 0:
                return False
        return True
