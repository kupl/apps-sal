class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxim = 0
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)): 
                if (nums[i]-1)*(nums[j]-1) > maxim: 
                    print(i)
                    print(j)
                    maxim = (nums[i]-1)*(nums[j]-1)
                    
        return maxim
