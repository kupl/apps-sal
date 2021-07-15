


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prv_code = self.grayCode(n-1)
        return prv_code + [2 ** (n-1) + x for x in reversed(prv_code)]
    
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ind=self.grayCode(n).index(start)
        
        
        return self.grayCode(n)[ind:]+self.grayCode(n)[:ind]
        
        

