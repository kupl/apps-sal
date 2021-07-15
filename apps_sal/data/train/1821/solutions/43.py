class Solution:
    def merge(self, nums1, nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            res.extend(nums1[i:])
        if j < len(nums2):
            res.extend(nums2[j:])
        
        return res
            
            
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        nums1 = self.sortArray(nums[:mid])
        nums2 = self.sortArray(nums[mid:])
        res = self.merge(nums1, nums2)
        return res
