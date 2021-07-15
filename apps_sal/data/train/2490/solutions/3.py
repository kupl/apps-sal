class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        array = [start+2*i for i in range(n)]
        res = start
        for i in range (1,len(array)):
            res ^=array[i]
            
        return res

