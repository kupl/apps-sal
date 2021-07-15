class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        nums = len(books)
        dp = [0 for _ in range(nums+1)]
        for i in range(nums):
            height = books[i][1]
            width = books[i][0]
            dp[i+1] = dp[i] + height
            for j in range(i)[i::-1]:
                print(i,j)
                if width + books[j][0] <= shelf_width:
                    height  = max(height, books[j][1])
                    dp[i+1]= min(height + dp[j], dp[i+1])    
                    width = width + books[j][0]
                else:
                    break
            print(f\"ans{dp[i+1]}\")
        return dp[-1]
                
            
