class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.singleNonDuplicateUtil(nums, 0, len(nums) - 1)

    def singleNonDuplicateUtil(self, nums, l, r):
        if l < r:
            mid = int((l + r) * 0.5)

            if mid - 1 >= 0 and nums[mid - 1] != nums[mid]:
                mid = mid - 1

            if (mid - l + 1) % 2 == 0:
                l = mid + 1
            else:
                r = mid

            return self.singleNonDuplicateUtil(nums, l, r)
        else:
            return nums[l]
