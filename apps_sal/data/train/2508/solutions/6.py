class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # my method 1: sort and compare different elements O(NlogN) O(n)
        heightsSorted = sorted(heights)
        
        # compare and acc different index
        ans = 0
        for i in range(len(heights)):
            if heights[i]!=heightsSorted[i]:
                ans += 1
        
        return ans
