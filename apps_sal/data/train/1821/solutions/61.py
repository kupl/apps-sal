class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if nums is None or len(nums) < 2:
            return nums
        
        return self.countSort(nums, len(nums))
    
    def countSort(self, nums, n):
        memo = collections.defaultdict(lambda: 0)
        
        for num in nums:
            memo[num] += 1
            
        answer = [None] * n
        currentIndex = 0
        
        for currentNum in range(-50000, 50001):
            
            if currentNum in memo:
                
                while memo[currentNum] > 0:
                    answer[currentIndex] = currentNum
                    currentIndex += 1
                    memo[currentNum] -= 1
                    
        return answer
                    

