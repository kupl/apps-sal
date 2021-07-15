class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [0]*(len(books)+1)
        for i in range(len(books)):
            maxheight = books[i][1]
            height = dp[i] + books[i][1]
            width = books[i][0]
            j = i-1
            while j >= 0 and width + books[j][0] <= shelf_width:
                maxheight = max(maxheight,books[j][1])
                width += books[j][0]
                height = min(height,dp[j]+maxheight)
                j -= 1
            dp[i+1] = height
        print(dp)
        return dp[-1]

