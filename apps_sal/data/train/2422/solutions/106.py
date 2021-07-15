class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        product_list = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product_list.append((nums[i]-1)*(nums[j]-1))
        return max(product_list)
        

