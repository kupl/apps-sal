class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def helper(start, end):
            if start >= end:
                return
            l = start
            r = end
            mid = l + (r - l) // 2
            pivot = nums[mid]
            while r >= l:
                while r >= l and nums[l] < pivot:
                    l += 1
                while r >= l and nums[r] > pivot:
                    r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(start, r)
            helper(l, end)
        
        helper(0, len(nums) - 1)
        return nums
