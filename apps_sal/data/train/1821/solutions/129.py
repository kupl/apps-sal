class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.mergeSortedArray(left, right)

    def mergeSortedArray(self, nums1, nums2):
        res = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                res.append(nums1.pop(0))
            else:
                res.append(nums2.pop(0))
        res += nums1 + nums2
        return res
