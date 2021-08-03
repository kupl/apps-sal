class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end = 0
        for _, _, e in trips:
            end = max(end, e)

        dp = [0 for _ in range(end)]
        for passengers, start, end in trips:
            for i in range(start, end):
                dp[i] += passengers
        return max(dp) <= capacity
