class Solution:
    def _isTriangle(self, queue):
        return queue[0] < queue[1] + queue[2]
    
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(key = lambda x: -x)
        
        nums = []
        
        for num in A:
            nums.append(num)
            
            if len(nums) == 3:
                if self._isTriangle(nums):
                    return sum(nums)
                nums.pop(0)
                
        return 0
