class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = int(len(nums)/2)
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    def merge(self, left, right):
        i = j = 0
        ret = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ret.append(left[i])
                i += 1
            elif right[j] <= left[i]:
                ret.append(right[j])
                j += 1
        ret.extend(left[i:])
        ret.extend(right[j:])
        return ret
