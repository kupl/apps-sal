class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]
            self.sortArray(l)
            self.sortArray(r)
            i = 0
            j = 0
            k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k += 1
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1
        return nums
