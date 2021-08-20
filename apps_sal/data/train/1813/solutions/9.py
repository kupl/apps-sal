class Solution:

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        memo = [float('inf')] * (len(books) + 1)
        memo[0] = 0
        for i in range(len(books)):
            width = shelf_width
            height = 0
            j = i
            while j >= 0 and width - books[j][0] >= 0:
                width -= books[j][0]
                height = max(height, books[j][1])
                memo[i + 1] = min(memo[i + 1], memo[j] + height)
                j -= 1
        return memo[-1]
