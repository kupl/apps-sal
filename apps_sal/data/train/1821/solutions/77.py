class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            else:
                q = nums[len(nums) // 2]
            l_nums = [n for n in nums if n < q]

            e_nums = [q] * nums.count(q)
            b_nums = [n for n in nums if n > q]
            return quicksort(l_nums) + e_nums + quicksort(b_nums)
        
        return quicksort(nums)

