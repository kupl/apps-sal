class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if nums == [] or len(nums) == 1:
            return nums
        if len(nums) == 2 and nums[0] < nums[1]:
            return nums
        first = 0
        middle = len(nums) // 2
        last = len(nums) - 1
        if nums[first] <= nums[middle] <= nums[last] or nums[last] <= nums[middle] <= nums[first]:
            (nums[first], nums[middle]) = (nums[middle], nums[first])
        elif nums[first] <= nums[last] <= nums[middle] or nums[middle] <= nums[last] <= nums[first]:
            (nums[first], nums[last]) = (nums[last], nums[first])
        pivot = 0
        cur = 0
        boarder = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[pivot]:
                boarder = i
                break
        cur = boarder + 1
        while cur < len(nums):
            if nums[cur] <= nums[pivot]:
                (nums[boarder], nums[cur]) = (nums[cur], nums[boarder])
                boarder += 1
            cur += 1
        left = nums[:boarder]
        right = nums[boarder:]
        nums = self.sortArray(left) + self.sortArray(right)
        return nums
