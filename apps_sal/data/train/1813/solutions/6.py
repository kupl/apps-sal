class Solution:

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        @lru_cache(None)
        def dp(i):
            if i == 0:
                return books[0][1]
            (max_height, thickness, ans) = (-float('inf'), 0, float('inf'))
            for j in range(i, -1, -1):
                (t, h) = books[j]
                if thickness + t <= shelf_width:
                    thickness += t
                    max_height = max(max_height, h)
                    ans = min(ans, dp(j - 1) + max_height if j > 0 else max_height)
                else:
                    break
            return ans
        n = len(books)
        for i in range(n):
            dp(i)
        return dp(n - 1)
