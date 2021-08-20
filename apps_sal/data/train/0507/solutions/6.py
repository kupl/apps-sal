class Solution:

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '\n         one = 0\n         for num in nums:\n             one = (~one&num)|(one&~num)\n         return one\n         '
        (l, r) = (0, len(nums) - 1)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid - 1]:
                if (r - mid) % 2 == 1:
                    l = mid + 1
                else:
                    r = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if (mid - l) % 2 == 1:
                    r = mid - 1
                else:
                    l = mid + 2
            else:
                return nums[mid]
        return nums[l]
