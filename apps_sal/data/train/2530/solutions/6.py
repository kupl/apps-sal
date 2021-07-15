class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        count = {}
        for t in time:
            
            if t%60 in count and (t%60==30 or t%60==0):
                res += count[t%60]
                
            elif (60 - t%60) in count:
                res += count[60-(t%60)]
            if t%60 in count:
                count[t%60] +=1
            else :
                count[t%60] = 1
            
        return res
