class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        for i in range(0 , len(nums)-1):
            for j in range(i+1 , len(nums)):
                product = (nums[i]-1) * (nums[j]-1)
                if product > max:
                    max = product
        return max
                
        # 0 1 2 3 4 5 len=6 
        # 2 3 5 6 8 9

