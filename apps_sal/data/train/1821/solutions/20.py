class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            return nums if nums[0] <= nums[1] else [nums[1], nums[0]]
        else:
            half = int(len(nums) / 2)
            a1 = self.sortArray(nums[:half])
            a2 = self.sortArray(nums[half:])
            nu = []
            olen = len(a1) + len(a2)
            while len(nu) < olen:
                if len(a1) == 0:
                    nu.append(a2.pop(0))
                elif len(a2) == 0:
                    nu.append(a1.pop(0))
                elif a1[0] < a2[0]:
                    nu.append(a1.pop(0))
                else:
                    nu.append(a2.pop(0))
            return nu
