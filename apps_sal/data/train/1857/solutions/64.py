class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        d = {}
        
        for r,c in reservedSeats: #O(M)
            if r not in d:
                d[r] = [1,1,1]
                
            if 2<= c <=5:
                d[r][0] = 0
            if 4 <= c <=7:
                d[r][1] = 0  
            if 6<= c<=9:
                d[r][2] = 0
        
        total = n*2
        res = 0
        for r in d:
            if sum(d[r])==0:  
                res += 2
            elif sum(d[r])<3:
                res += 1
                
        return total - res
        

