class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        dp = [0]*1000
        
        for trip in trips:
            num, s, e = trip[0], trip[1], trip[2]
            for i in range(s, e):
                dp[i] += num
        print(dp)
        for i in range(len(dp)):
            if dp[i] > capacity:
                return False
            
        return True

