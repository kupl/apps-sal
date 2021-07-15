class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memory = [0] * 60
        res = 0
        
        for t in time:
            res += memory[(t % 60) % 60]
            memory[(60 - t) % 60] += 1
            
        return res
