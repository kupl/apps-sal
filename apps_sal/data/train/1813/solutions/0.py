class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [inf] * (n+1)
        dp[0] = 0
        ret = inf
        for i in range(1, n+1):
            mx = 0
            cur = 0
            for j in range(i, 0, -1):
                cur += books[j-1][0]
                if cur > shelf_width:
                    break
                mx = max(mx, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + mx)
        return dp[-1]

