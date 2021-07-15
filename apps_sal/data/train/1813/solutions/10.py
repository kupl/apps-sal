class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        # n = len(books)
        # @lru_cache(None)
        # def dfs(i, w, h):
        #     if i >= n:
        #         return h
        #     return min(h + dfs(i + 1, books[i][0], books[i][1]), float('inf') if w + books[i][0] > shelf_width else dfs(i + 1, w + books[i][0], max(h, books[i][1])))
        # return dfs(0, 0, 0)
        
        n = len(books)
        dp = [0] + [float('inf')] * n
        for p in range(1, n + 1):
            i = p
            w = h = 0
            while i > 0 and w + books[i-1][0] <= shelf_width:
                w += books[i-1][0]
                h = max(h, books[i-1][1])
                dp[p] = min(dp[p], dp[i-1] + h)
                i -= 1
        return dp[-1]
        
        
        # n = len(books)
        # dp = [0] + [float('inf')] * n
        # for p in range(1, n + 1):
        #     i = p
        #     w = h = 0
        #     while i > 0 and w + books[i-1][0] <= shelf_width:
        #         w += books[i-1][0]
        #         h = max(h, books[i-1][1])
        #         dp[p] = min(dp[p], dp[i-1]+h)
        #         i -= 1
        # return dp[-1]
        
        # n = len(books)
        # @lru_cache(None)
        # def dfs(i, w, h):
        #     if i >= n:
        #         return h
        #     return min(h + dfs(i + 1, books[i][0], books[i][1]), float('inf') if w + books[i][0] > shelf_width else dfs(i + 1, w + books[i][0], max(h, books[i][1])))
        # return dfs(0, 0, 0)
    
                
            

