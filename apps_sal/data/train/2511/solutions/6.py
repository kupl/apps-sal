class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        nums = {}
        for i in A:
            if i not in list(nums.keys()):
                nums[i] = 1
            else:
                nums[i] += 1
        
        print(nums)
        
        for i in nums:
            if nums[i] == len(A) / 2:
                return i
            

