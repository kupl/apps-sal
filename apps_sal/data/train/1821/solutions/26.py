class Solution:

    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ret = []
        ix1 = 0
        ix2 = 0
        while ix1 != len(arr1) and ix2 != len(arr2):
            if arr1[ix1] < arr2[ix2]:
                ret.append(arr1[ix1])
                ix1 += 1
            else:
                ret.append(arr2[ix2])
                ix2 += 1
        if ix1 < len(arr1):
            ret.extend(arr1[ix1:])
        else:
            ret.extend(arr2[ix2:])
        return ret

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
