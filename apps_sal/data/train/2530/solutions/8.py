class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        d = {}
        for x in range(len(time)):
            
            time[x] %= 60
            if time[x] in d:
                d[time[x]] += 1
            else:
                d[time[x]] = 1
        cc = 0

        for x in time:
            
            if 60 - x in d:
 
                d[x] -= 1
                cc += d[60-x]
                if d[x] == 0:
                    del d[x]
            elif x == 0:
                d[x] -= 1
                cc += d[x]
                if d[x] == 0:
                    del d[x]

        return cc
            
            
            
        
        
                    
        
    
    

