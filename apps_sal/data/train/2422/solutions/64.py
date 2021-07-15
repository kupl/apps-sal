class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        second_largest = 0
        largest = 0
        max_product = 0
        for index1 in range(len(nums)-1):
            for index2 in range(index1+1, len(nums)):
                product = nums[index1] * nums[index2]
                if product > max_product:
                    max_product = product
                    if nums[index1] > nums[index2]:
                        largest, second_largest = nums[index1], nums[index2]
                    else:
                        largest, second_largest = nums[index2], nums[index1]
        return ((largest-1) * (second_largest-1))

