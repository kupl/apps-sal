import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(nums):
            if len(nums) == 0:
                return []
            pivot = random.choice(nums)

            less = [x for x in nums if x < pivot]
            eq = [x for x in nums if x == pivot]
            more = [x for x in nums if x > pivot]

            return quick(less) + eq + quick(more)
        return quick(nums)

