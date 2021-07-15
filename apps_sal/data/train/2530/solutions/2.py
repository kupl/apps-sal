class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        count = [0]*60
        for t in time:
            
            if (t%60==30 or t%60==0):
                res += count[t%60]
                
            else:
                res += count[60-(t%60)]
            
            count[t%60] +=1
            
            
        return res
