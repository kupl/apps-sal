\"\"\"

\"\"\"

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        
        books_len = len(books)
        
        @lru_cache(None)
        def dp(i):
            if i == books_len:
                return 0
            
            width, height = 0, 0
            
            result = []
            
            while i < books_len and width <= shelf_width:
                width += books[i][0]
                height = max(height, books[i][1])
                if width <= shelf_width:
                    result.append(height + dp(i+1))
                i += 1
            
            return min(result)    
        
        return dp(0)
