class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        self.shelf = defaultdict(list)
        
        @lru_cache(None)
        def helper(i):
            if i == len(books):
                return 0
            
            width = 0
            height = 0
            out = float('inf')            
            
            while width < shelf_width and i < len(books):
                w,h = books[i]                
                width += w
                
                if width > shelf_width: # went over when added this new book
                    break
                    
                # max height of this shelf with new book added
                height = max(height, h) 
                
                # see how much the total height others are if we include the new book
                # in this shelf
                others = helper(i+1) 
                
                # if height of current shelf+ total height of other books is minimum
                # save it.
                out = min(height+others, out) 
                i+= 1
            return out
        
        out = helper(0)
        return out
            
            

