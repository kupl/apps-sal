class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = sort(nums[:mid])
            right = sort(nums[mid:])
            i, j = 0, 0
            res = []
            while i < mid and j < len(nums) - mid:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            if i < mid:
                res += left[i:]
            if j < len(nums) - mid:
                res += right[j:]

            return res

        return sort(nums)
