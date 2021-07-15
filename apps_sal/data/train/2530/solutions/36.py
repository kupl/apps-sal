class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = {}
        ans = 0
        
        for i in range(len(time)):
            t = time[i] % 60
            other = 0 if t == 0 else 60 - t
            if other in count:
                ans += count[other]
            count[t] = count.get(t, 0) + 1
        
        return ans
        

