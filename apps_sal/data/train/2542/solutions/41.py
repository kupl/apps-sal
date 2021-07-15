class Solution:
    
    def check(self, B):
        self.B = B
        result = []
        for i in range(len(self.B) - 1):
            if self.B[i] <= self.B[i+1]:
                result.append(True)
            else:
                result.append(False)
        
        final = all(result)
        return final
    
    
    def isMonotonic(self, A: List[int]) -> bool:
        
        a = []
        
        a.append(self.check(A))
        a.append(self.check(A[::-1]))
        
        b = any(a)

        return b        

