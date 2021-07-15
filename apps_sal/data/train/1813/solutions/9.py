class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        memo = [float('inf')] * (len(books)+1)
        memo[0] = 0
        
        for i in range(len(books)):
            width = shelf_width
            height = 0 
            j = i
            # to determine the minimum height up to the ith book, 
            # we need te examine all possible books which in the same level as the ith book up to the ith book
            # the later books which may be in the same level as the ith book will be examined later when it is introduced.
            while j >=0 and width - books[j][0]>=0:      
                width -= books[j][0]
                height = max(height, books[j][1])
                memo[i+1] = min(memo[i+1], memo[j]+height)
                j -= 1
        
        return memo[-1]
