class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        left = self.sortArray(left)
        right = self.sortArray(right)
        res = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        res = res + left + right
        return res
