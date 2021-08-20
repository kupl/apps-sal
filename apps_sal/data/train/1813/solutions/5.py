class Solution:

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        books_len = len(books)

        @lru_cache(None)
        def dp(i):
            if i == books_len:
                return 0
            (width, height, result) = (0, 0, float('inf'))
            while i < books_len and width <= shelf_width:
                width += books[i][0]
                height = max(height, books[i][1])
                if width <= shelf_width:
                    result = min(result, height + dp(i + 1))
                i += 1
            return result
        return dp(0)
