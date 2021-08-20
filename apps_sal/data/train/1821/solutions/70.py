class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[int(len(nums) / 2)]
            L = []
            M = []
            R = []
            for n in nums:
                if n < pivot:
                    L.append(n)
                elif n > pivot:
                    R.append(n)
                else:
                    M.append(n)
            return self.sortArray(L) + M + self.sortArray(R)
