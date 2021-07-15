class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for idx in range(2, n + 1):
            for idx2 in range(1, idx):
                if idx2 == 1 or self.get_gcd(idx, idx2) == 1:
                    res.append('{}/{}'.format(idx2, idx))
        return res
    
    def get_gcd(self, num1, num2):
        if num1 % num2 == 0:
            return num2
        return self.get_gcd(num2, num1 % num2)

