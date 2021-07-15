import math

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        current = label
        res = [current]
        
        while current != 1:
            current //= 2
            depth = int(math.log2(current))
            
            nodes = [i for i in range(2**depth, 2**(depth+1))]
            
            idx = nodes.index(current)
            current = list(reversed(nodes))[idx]
            res.append(current)
            
        return reversed(res)
            
            
            
            
            
            

