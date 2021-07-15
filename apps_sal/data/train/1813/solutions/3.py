class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        heights = [0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            width  = books[i-1][0]
            height = books[i-1][1]
            heights[i] = heights[i-1] + height
            j = i-1
            while j > 0 and width + books[j-1][0] <= shelf_width:
                height = max(height, books[j-1][1])
                width+=books[j-1][0]
                heights[i] = min(heights[i], heights[j-1] + height)
                j-=1
        print(f'{heights}')
        return heights[-1]

