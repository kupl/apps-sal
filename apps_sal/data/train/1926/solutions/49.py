class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        add1 = num + 1
        add2 = num + 2
        
        start = floor(sqrt(add2))
        
        for i in range(start, 0, -1):
            x1, r1 = divmod(add1, i)
            x2, r2 = divmod(add2, i)
            
            if r1 == 0:
                return i, x1
            if r2 == 0:
                return i, x2

