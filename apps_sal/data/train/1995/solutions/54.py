class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dp = [capacity] * 1000
        for trip in trips:
            for loc in range(trip[1], trip[2]):
                dp[loc] -= trip[0]
        return not (min(dp) < 0)
